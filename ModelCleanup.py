import logging
import os
import sys
import time

import TM1py.Exceptions
from TM1py import TM1Service

from base_settings import APP_NAME, APPLICATION_PATH
FILENAME = APP_NAME + '.log'
LOG_FILE = os.path.join(APPLICATION_PATH, FILENAME)


def configure_logging() -> None:
    """
    Setup logging for actions taken
    :return: None
    """
    logging.basicConfig(
        filename=LOG_FILE,
        format="%(asctime)s - " + APP_NAME + " - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    # also log to stdout
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))


def perform_clean(file: str, config: dict, instance: str) -> None:
    """
    Read CSV file and begin working through the items to remove
    :param file: str filename including path
    :param config: dict to use for TM1PY
    :param instance: string representation of server name
    :return: None
    """
    configure_logging()
    start = time.perf_counter()
    logging.info(f"Process started for Instance: '{instance}', using file: '{file}'")
    with open(file, 'r') as parser:
        objects = parser.read().splitlines()
    try:
        with TM1Service(**config) as tm1:
            for obj in objects:
                try:
                    typ, obj = obj.split(':')
                    if typ.lower() == '-p':
                        if tm1.processes.exists(name=obj):
                            tm1.processes.delete(name=obj)
                            logging.info(f"Process: '{obj}' deleted")
                        else:
                            logging.error(f"Process: '{obj}' does not exist")
                    if typ.lower() == '-c':
                        if tm1.cubes.exists(cube_name=obj):
                            tm1.cubes.delete(cube_name=obj)
                            logging.info(f"Cube: '{obj}' deleted")
                        else:
                            logging.error(f"Cube: '{obj}' does not exist")
                    if typ.lower() == '-d':
                        if tm1.dimensions.exists(dimension_name=obj):
                            tm1.dimensions.delete(dimension_name=obj)
                            logging.info(f"Dimension: '{obj}' deleted")
                        else:
                            logging.error(f"Dimension: '{obj}' does not exist")
                    if typ.lower() == '-s':
                        dim, sub = obj.split('&')
                        if tm1.subsets.exists(dimension_name=dim, subset_name=sub):
                            tm1.subsets.delete(dimension_name=dim, subset_name=sub)
                            logging.info(f"Subset: '{sub}' was deleted from dimension: '{dim}'")
                        else:
                            logging.error(f"Subset: '{sub}' from dimension: '{dim}' not found")
                    if typ.lower() == '-v':
                        cube, view = obj.split('&')
                        if tm1.views.exists(cube_name=cube, view_name=view):
                            tm1.views.delete(cube_name=cube, view_name=view)
                            logging.info(f"View: '{view}' was deleted from Cube: '{cube}'")
                        else:
                            logging.error(f"View: '{view}' from cube: '{cube}' was not found")
                except TM1py.Exceptions.TM1pyNotAdminException:
                    logging.error("ADMIN permissions required")
                except TM1py.Exceptions.TM1pyException as t:
                    if 'DimensionIsBeingUsedByCube' in t.message:
                        logging.error(f"Dimension '{obj}' used by existing cube")
                        continue
                    elif 'SubsetIsBeingUsedByView' in t.message:
                        logging.error(f"Subset: {sub} cannot be deleted from dimension: '{dim}'"
                                      f" because it is being used in a view")
                        continue
                    else:
                        logging.error(str(t))
    except Exception as e:
        logging.error(str(e))
    end = time.perf_counter()
    logging.info(f"Processes completed in {round(end - start, 2)} seconds")
