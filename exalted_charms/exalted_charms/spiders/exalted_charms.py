from pathlib import Path

import scrapy
import custom_funtions.value_functions as vf


def sift_thru_keys(list_of_keys_raw):
    true_keys = []

    for key in list_of_keys_raw:
        if key in true_keys:
            break
        else:
            true_keys.append(key)

    true_keys.append("Description")

    return true_keys


def sift_thru_values(list_of_var_raw, true_keys):
    new_list_of_var = vf.remove_enter(list_of_var_raw)
    new_list_of_var = vf.find_unbolded(new_list_of_var)
    new_list_of_var = vf.remove_excess(new_list_of_var, true_keys)
    patterns = ['^:.*\d+m', "^:.*\d+wp", ':\s*[-—];\s', '^:.*motes']
    cost_list = vf.find_beggining(new_list_of_var, patterns)
    list_of_list = vf.organize_data_per_charm(new_list_of_var, cost_list)
    list_of_list = vf.combine_description_indices(list_of_list)
    return list_of_list


def create_dictionary(list_of_list,
                      true_keys,
                      list_of_titles,
                      charm_type):
    all_charms = []
    single_charm = {}

    for index1, charm in enumerate(list_of_list):
        single_charm.update({
            "Title": list_of_titles[index1],
            "Type of Exalt": charm_type[0].capitalize(),
            "Abilities": charm_type[1].capitalize()
        })

        for index2, part in enumerate(charm):
            single_charm.update({
                true_keys[index2]: part
            })

        all_charms.append(single_charm)
        single_charm = {}

    return all_charms


class CharmsSpider(scrapy.Spider):
    name = "charms"
    # url = [
    #     "http://exalted275e.wikidot.com/sidereal-archery"
    # ]

    def start_requests(self):
        urls = [
            "http://exalted275e.wikidot.com/sidereal-archery",
            "http://exalted275e.wikidot.com/sidereal-martial-arts",
            "http://exalted275e.wikidot.com/sidereal-melee",
            "http://exalted275e.wikidot.com/sidereal-thrown",
            "http://exalted275e.wikidot.com/sidereal-war",
            "http://exalted275e.wikidot.com/sidereal-integrity",
            "http://exalted275e.wikidot.com/sidereal-performance",
            "http://exalted275e.wikidot.com/sidereal-presence",
            "http://exalted275e.wikidot.com/sidereal-resistance",
            "http://exalted275e.wikidot.com/sidereal-survival",
            "http://exalted275e.wikidot.com/sidereal-craft",
            "http://exalted275e.wikidot.com/sidereal-investigation",
            "http://exalted275e.wikidot.com/sidereal-lore",
            "http://exalted275e.wikidot.com/sidereal-medicine",
            "http://exalted275e.wikidot.com/sidereal-occult",
            "http://exalted275e.wikidot.com/sidereal-athletics",
            "http://exalted275e.wikidot.com/sidereal-awareness",
            "http://exalted275e.wikidot.com/sidereal-dodge",
            "http://exalted275e.wikidot.com/sidereal-larceny",
            "http://exalted275e.wikidot.com/sidereal-stealth",
            "http://exalted275e.wikidot.com/sidereal-bureaucracy",
            "http://exalted275e.wikidot.com/sidereal-linguistics",
            "http://exalted275e.wikidot.com/sidereal-ride",
            "http://exalted275e.wikidot.com/sidereal-sail",
            "http://exalted275e.wikidot.com/sidereal-socialize",
            "http://exalted275e.wikidot.com/solar-archery",
            "http://exalted275e.wikidot.com/solar-martial-arts",
            "http://exalted275e.wikidot.com/solar-melee",
            "http://exalted275e.wikidot.com/solar-thrown",
            "http://exalted275e.wikidot.com/solar-war",
            "http://exalted275e.wikidot.com/solar-integrity",
            "http://exalted275e.wikidot.com/solar-performance",
            "http://exalted275e.wikidot.com/solar-presence",
            "http://exalted275e.wikidot.com/solar-resistance",
            "http://exalted275e.wikidot.com/solar-survival",
            "http://exalted275e.wikidot.com/solar-craft",
            "http://exalted275e.wikidot.com/solar-investigation",
            "http://exalted275e.wikidot.com/solar-lore",
            "http://exalted275e.wikidot.com/solar-medicine",
            "http://exalted275e.wikidot.com/solar-occult",
            "http://exalted275e.wikidot.com/solar-athletics",
            "http://exalted275e.wikidot.com/solar-awareness",
            "http://exalted275e.wikidot.com/solar-dodge",
            "http://exalted275e.wikidot.com/solar-larceny",
            "http://exalted275e.wikidot.com/solar-stealth",
            "http://exalted275e.wikidot.com/solar-bureaucracy",
            "http://exalted275e.wikidot.com/solar-linguistics",
            "http://exalted275e.wikidot.com/solar-ride",
            "http://exalted275e.wikidot.com/solar-sail",
            "http://exalted275e.wikidot.com/solar-socialize",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        list_of_keys_raw = response.css(
            "#page-content p strong::text").getall()
        list_of_values_raw = response.xpath(
            '//div[@id="page-content"]//p//text()').getall()
        list_of_titles = response.css("#page-content h2 span::text").getall()
        true_keys = sift_thru_keys(list_of_keys_raw)
        list_of_values = sift_thru_values(list_of_values_raw, true_keys)
        charm_type = vf.get_charm_type(response.url)
        all_charms = create_dictionary(
            list_of_values,
            true_keys,
            list_of_titles,
            charm_type)

        all_charms = vf.clean_up(all_charms)

        for charm in all_charms:
            yield charm

        # charm_type = response.url.split("/")[-1]
        # filename = f"{charm_type[6:]}-charms.html"
        # Path(filename).write_bytes(response.body)
        # self.log(f"Saved file {filename}")
