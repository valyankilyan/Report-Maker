title_keys_path = 'title_keys'
replace_dictionary = {}

with open(title_keys_path) as f:
    for line in f:
        if line.startswith('#') or not line.strip():
            continue
        key, value = line.split('=', 1)
        replace_dictionary[key] = value

