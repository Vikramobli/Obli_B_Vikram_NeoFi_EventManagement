from deepdiff import DeepDiff

def get_diff(old, new):
    return DeepDiff(old, new, ignore_order=True).to_dict()