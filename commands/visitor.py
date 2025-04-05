from config import conf
from pprint import pprint

def visitor(args):
    subcommand_map = {
        "show": visitor_show,
        "add": visitor_add,
        "delete": visitor_delete
    }
    subcommand_map.get(args.subcommand, visitor_show)(args)

def visitor_show(args):
    pprint(conf.plates)

def visitor_add(args):
    conf.plates.update({
        args.name: args.plate
    })
    conf.save_to_json()
    print(f"Added visitor '{args.name}' with plate '{args.plate}'")

def visitor_delete(args):
    try:
        plate = conf.plates.pop(args.name)
        conf.save_to_json()
        print(f"Deleted visitor '{args.name}' with plate '{plate}'")
    except KeyError:
        print(f"No visitor named '{args.name}'")
