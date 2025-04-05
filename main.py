import argparse
from config import conf
import commands

parser = argparse.ArgumentParser(description="Parkon Registration", prog="parkon")
subparsers = parser.add_subparsers(dest="command")

# Register command
register_sp = subparsers.add_parser("register", help="Register a visitor")
register_sp.add_argument("-n", "--name", type=str, help="Visitor name", required=True)
register_sp.add_argument("-t", "--duration", type=str, help="Parking duration", choices=conf.durations, default="12")
register_sp.add_argument("-e", "--email", type=str, help="Confirmation email recipient", required=False, default=conf.email)
register_sp.add_argument("-y", "--autosubmit", action="store_true", help="Automatically hit send")
register_sp.add_argument("-s", "--noemail", action="store_true", help="Do not send a confirmation email")
register_sp.add_argument("-i", "--headless", action="store_true", help="Run in headless mode (will autosubmit)")

# Config command
config_sp =  subparsers.add_parser("config", help="View or change configuration")
config_ssps = config_sp.add_subparsers(dest="subcommand")

config_show_sp = config_ssps.add_parser("show", help="Show configuration values")

config_set_sp = config_ssps.add_parser("set", help="Set configuration value")
config_set_sp.add_argument("-k", "--key", type=str, help="Configuration key", required=True)
config_set_sp.add_argument("-v", "--value", type=str, help="Configuration value", required=True)

# Visitor command
visitor_sp =  subparsers.add_parser("visitor", help="View or change visitors")
visitor_ssps = visitor_sp.add_subparsers(dest="subcommand")

config_show_sp = visitor_ssps.add_parser("show", help="Show visitors")

visitor_add_sp = visitor_ssps.add_parser("add", help="Add or update visitor")
visitor_add_sp.add_argument("-n", "--name", type=str, help="Visitor name", required=True)
visitor_add_sp.add_argument("-p", "--plate", type=str, help="License plate number", required=True)

visitor_add_sp = visitor_ssps.add_parser("delete", help="Delete visitor")
visitor_add_sp.add_argument("-n", "--name", type=str, help="Visitor name", required=True)

command_map = {
    "register": commands.register,
    "config": commands.config,
    "visitor": commands.visitor
}

args = parser.parse_args()

try:
    command_map.get(args.command, lambda _: parser.print_help())(args)
except:
    exit(1)
