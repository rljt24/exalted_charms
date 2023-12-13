import re


def remove_enter(list_value):
    for item in list_value:
        if item == '\n':
            list_value.pop(list_value.index(item))
    return list_value


def remove_excess(charms_list, true_keys_list):
    for item in charms_list:
        if item in true_keys_list:
            charms_list.pop(charms_list.index(item))
    return charms_list


def find_unbolded(charms_list):
    for index, item in enumerate(charms_list):
        if re.search("^Cost:", item):
            charms_list[index] = ": -; "
    return charms_list


def find_beggining(charms_list, patterns):
    cost_list = []
    for text in charms_list:
        if re.search(patterns[0], text) or re.search(patterns[1], text) or re.match(patterns[2], text) or re.search(patterns[3], text):
            cost_list.append(text)
    return cost_list


def organize_data_per_charm(list_of_data, beggining_list):
    list_of_list = []
    append_list = []

    for index_text, text in enumerate(list_of_data):
        if text in beggining_list:
            if not append_list:
                append_list.append(text)
            else:
                list_of_list.append(append_list)
                append_list = []
                append_list.append(text)
        else:
            append_list.append(text)
        if index_text == len(list_of_data)-1:
            list_of_list.append(append_list)

    return list_of_list


def combine_description_indices(list_of_list):
    for ind1, charm in enumerate(list_of_list):
        for ind2, part in enumerate(charm):
            if re.search(r'^\n', part):
                start_index = ind2
                end_index = len(charm)-1
                break

        new_string = ''

        if start_index == end_index:
            continue
        else:
            for part in charm[start_index:]:
                new_string = new_string + part

            new_charm = charm[:start_index+1]
            new_charm[-1] = new_string
            list_of_list[ind1] = new_charm

    return list_of_list


def get_charm_type(url):
    charm_type = url.split("/")[-1]
    charm_type = charm_type.split("-")
    if len(charm_type) > 2:
        exalt_type = charm_type.pop(0)
        charm_type = ' '.join(charm_type)
        charm_type = [exalt_type, charm_type]

    return charm_type


def clean_up(all_charms):
    for charm_object in all_charms:
        for key, value in charm_object.items():
            # print(re.search(r"^: ", value))
            if re.search(r"^: ", value):
                value = re.sub(r"^: ", "", value)

            if re.search(r';\s?$', value):
                value = re.sub(r';\s?$', '', value)

            if re.search(r"^\n", value):
                value = re.sub(r"^\n", '', value)

            if key == "Mins":
                value_list = value.split(", ")
                value_dict = {}
                for part in value_list:
                    part_list = part.split(" ")
                    if len(part_list) == 2:
                        value_dict.update({
                            part_list[0]: int(part_list[-1])
                        })
                    else:
                        sub_string = part_list[0] + ' ' + part_list[1]
                        value_dict.update({
                            sub_string: int(part_list[-1])
                        })
                value = value_dict

            if key == "Keywords" or key == "Prerequisite Charms":
                value = value.split(", ")

            charm_object[key] = value

    return all_charms
