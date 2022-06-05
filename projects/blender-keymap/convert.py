import bindings
from compile import FullyQualifiedCommand, KeyCombo
import yaml

allcommands = []
commandsmap = {}


def register_command(combo, cmd):
    combo = str(combo)
    if combo in commandsmap:
        commandsmap[combo].append(cmd.to_dict())
    else:
        commandsmap[combo] = [cmd.to_dict()]


for context_group in bindings.keyconfig_data:
    context = context_group[0]
    types = context_group[1]
    specs = context_group[2]
    for item in specs["items"]:
        command = item[0]
        keycombo = KeyCombo.from_dict(item[1])
        options = item[2]
        fqcommand = FullyQualifiedCommand(
            context, types["space_type"], types["region_type"], command
        )
        allcommands.append(fqcommand)
        register_command(keycombo, fqcommand)


print(yaml.dump(commandsmap))
