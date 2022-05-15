from dataclasses import dataclass


@dataclass
class FullyQualifiedCommand:
    context: str
    space_type: str
    region_type: str
    command: str
    options: dict = None

    def __str__(self):
        return (
            "{ "
            + f"'context': '{self.context}', "
            + f"'space_type': '{self.space_type}', "
            + f"'region_type': '{self.region_type}', "
            + f"'command': '{self.command}', "
            + f"'options': '{self.options}' "
            + "}"
        )


@dataclass(frozen=True)
class KeyCombo(dict):
    type: str
    value: str
    alt: bool
    shift: bool
    ctrl: bool
    oskey: bool

    @classmethod
    def from_dict(cls, obj):
        return KeyCombo(
            type=obj["type"],
            value=obj["value"],
            alt=obj.get("alt", False),
            shift=obj.get("shift", False),
            ctrl=obj.get("ctrl", False),
            oskey=obj.get("oskey", False),
        )

    @classmethod
    def from_str(cls, s):
        value, rest = s.split(" ")
        oskey = "cmd-" in rest
        alt = "option-" in rest
        shift = "shift-" in rest
        ctrl = "ctrl-" in rest
        type = (
            rest.replace("cmd-", "")
            .replace("option-", "")
            .replace("shift-", "")
            .replace("ctrl-", "")
        )
        return KeyCombo(
            value=value, oskey=oskey, alt=alt, shift=shift, ctrl=ctrl, type=type
        )

    def to_dict(self):
        return {
            "value": self.value,
            "type": self.type,
            "alt": self.alt,
            "oskey": self.oskey,
            "shift": self.shift,
            "ctrl": self.ctrl,
        }

    def __str__(self):
        s = self.value + " "
        if self.oskey:
            s += "cmd-"
        if self.alt:
            s += "option-"
        if self.shift:
            s += "shift-"
        if self.ctrl:
            s += "ctrl-"
        s += self.type
        return s


def get_context_names(entries):
    names = set()
    for entry in entries:
        commands = entry[1]
        for command in commands:
            names.add(command["context"])
    return names


def compile(entries):
    context_names = get_context_names(entries)
    output = []
    for context_name in context_names:
        context = [context_name]
        context_types = {}
        items = []
        for entry in entries:
            keycombo = KeyCombo.from_str(entry[0]).to_dict()
            for cmd in entry[1]:
                context_types["space_type"] = cmd["space_type"]
                context_types["region_type"] = cmd["region_type"]
                nextitem = (cmd["command"], keycombo, cmd["options"])
                items.append(nextitem)

        context.append(context_types)
        context.append({"items": items})
        output.append(tuple(context))
        return output
