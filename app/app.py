import argparse
import logging
import logging.config
from pathlib import Path

import yaml
from dotenv import load_dotenv

from browsers import Browsers
from form_filler import FormFiller


# with open('logging.yml', 'r') as f:
#     config = yaml.safe_load(f.read())
#     logging.config.dictConfig(config)

logger = logging.getLogger()

load_dotenv(dotenv_path=Path("env/.env"))


def main():
    arg_parse = argparse.ArgumentParser(description="Demo Selenium script")
    arg_parse.add_argument("--browser", choices=Browsers._member_names_, default=Browsers.FIREFOX.name, help="Browser to use")
    args = arg_parse.parse_args()

    form_filler = FormFiller(args.browser)
    form_filler.run()


if __name__ == "__main__":
    main()
