from config import conf
from dataclasses import asdict
from pprint import pprint

def config(args):
    subcommand_map = {
        "show": config_show,
        "set": config_set,
    }
    subcommand_map.get(args.subcommand, config_show)(args)

def config_show(args):
    pprint(asdict(conf), sort_dicts=False, compact=True)

def config_set(args):
    if args.key not in asdict(conf):
        print(f"The configuration '{args.key}' does not exist")
        raise RuntimeError

    if args.key not in (modifiable_keys := ["url", "email"]):
        print(f"The configuration '{args.key}' is read only, modifiable keys: {modifiable_keys}")
        raise RuntimeError
    
    conf.__dict__[args.key] = str(args.value)
    conf.save_to_json()
    print(f"Set '{args.key}' to '{args.value}'")
