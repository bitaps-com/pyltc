import importlib
import importlib.util
from types import ModuleType


def specialize(module_name, owner, *overrides):
    original = importlib.import_module(module_name)
    spec = importlib.util.spec_from_file_location(owner, original.__file__)
    if spec is None or spec.loader is None:
        raise ImportError("Cannot isolate upstream module: %s" % module_name)
    private = importlib.util.module_from_spec(spec)
    private.__package__ = original.__package__
    spec.loader.exec_module(private)
    for override in overrides:
        values = vars(override) if isinstance(override, ModuleType) else override
        names = values.get("__all__", [name for name in values if not name.startswith("_")])
        private.__dict__.update((name, values[name]) for name in names)
    return private
