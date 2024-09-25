# __main__.py
# Author: DaYuan Tan, dr.dayuantan at gmail dot com
# Last Modified: 2024-09-25

"""Extract PDF contents with the magic of GPT.

Usage:
------

    $ realpython [options]

Available options are:

    -h, --help         Show this help


Contact:
--------

- https://github.com/DayuanTan/pdf-gpt
- Author: DaYuan Tan, dr.dayuantan at gmail dot com

More information is available at:

- https://github.com/DayuanTan/pdf-gpt


Version:
--------

- pdf-gpt v0.1.0
"""
import sys


def main() -> None:
    """Extract content from PDF files."""
    opts = [o for o in sys.argv[1:] if o.startswith("-")]
    
    # Show help message
    if "-h" in opts or "--help" in opts:
        print(__doc__)
        raise SystemExit()
    

if __name__ == "__main__":
    main()