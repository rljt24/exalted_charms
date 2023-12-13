import re
import pprint

charms_list = ['Cost', ': 3m; ', 'Mins', ': Medicine 1, Essence 1;', '\n', 'Type', ': Simple (Speed 5)', '\n', 'Keywords', ': Touch', '\n', 'Duration', ': Instant', '\n', 'Prerequisite Charms', ': None', "\nThose who serve the Solars faithfully need know no pain. The recipient of this Charm feels a temporary euphoria qualitatively similar to an opium high. This Charm cancels up to three points of the target’s penalties from Sickness, Poison, Crippling effects, and wound penalties for (Solar's Essence) hours. ", 'Touch of Blissful Release', ' is not addictive to the target.', 'Cost', ': 5m; ', 'Mins', ': Medicine 2, Essence 1;', '\n', 'Type', ': Supplemental', '\n', 'Keywords', ': Touch', '\n', 'Duration', ': Indefinite', '\n', 'Prerequisite Charms', ': None', '\nTie a Solar physician and a man dying of the plague to an anchor and cast them into a stormy sea, still the Solar may have the ingenuity to heal the victim. This Charm supplements a Medicine-based action to treat a patient. It does not reduce the time required for medical treatment, but otherwise allows the Solar to treat patients in unfavorable conditions without medicines, penalties, or a stunt. The medical shortcuts involved depend on the Exalt in question. Some learn special pressure points, others channel raw Essence to heal, and still others inspire new strength in their patients through words and actions.', 'Cost', ': 10m; ', 'Mins', ': Medicine 2, Essence 2;', '\n', 'Type', ': Supplemental', '\n', 'Keywords', ': Touch', '\n', 'Duration', ': Instant', '\n', 'Prerequisite Charms', ': None', '\nSolar physicians can speed a patient’s recovery from even the most terrible wounds. This Charm supplements a dramatic action to treat, monitor and tend to the patient. This action requires one hour spent without a stunt or a Charm. The Solar’s player rolls (Intelligence + Medicine). This Charm replaces the normal benefits of medical care, instead allowing the target to recover a number of lethal or bashing health levels equal to the number of successes instantly. If the target spends the day resting, the target recovers a number of additional lethal and bashing health levels equal to the Solar’s permanent Essence. No patient can benefit from this Charm more than once per day.', '\nAt Essence 3+ this Charm has no limit to to how many times it can be used on the same patient each day.', 'Cost', ': 5m; ', 'Mins', ': Medicine 2, Essence 2;', '\n', 'Type', ': Simple (Speed 5)', '\n', 'Keywords', ': Obvious, Stackable, Touch', '\n', 'Duration', ': Indefinite', '\n', 'Prerequisite Charms', ': Wound-Mending Care Technique', "\nThe Essence of the Solar Exalted fills others with new life. The efforts of the Solar healer inspire the injured, the broken, the faltering and the weak to rise and take their burdens up again. This Charm gives the target a number of temporary -1 health levels equal to the user’s Essence. These health levels are the first lost when the character takes damage, and they are never healed back. When the Solar stops committing Essence to this Charm, the additional health levels fade without ill effect, whether or not they have been lost. This doesn't stack with similar powers or other Exalts using this Charm.", 'Cost', ': 5m; ', 'Mins', ': Medicine 3, Essence 2;', '\n', 'Type', ': Supplemental', '\n', 'Keywords', ': Obvious, Touch', '\n', 'Duration', ': Instant', '\n', 'Prerequisite Charms', ': Contagion-Curing Touch, Wound-Mending Care Technique', '\nGreat Solar healers can draw the poison from even unnatural wounds. This Charm enhances a dramatic action to treat, monitor and tend to the patient. This action requires one hour without a stunt or a Charm. This Charm replaces the normal benefits of medical care. Instead, the Solar’s player rolls (Intelligence + Medicine). If she succeeds, the Solar converts all of the target’s aggravated wound levels to lethal wound levels.', 'Cost', ': 1m; ', 'Mins', ': Medicine 1, Essence 1;', '\n', 'Type', ': Reflexive', '\n', 'Keywords', ': Mirror (Pitless Triage Judgement)', '\n', 'Duration', ': Instant', '\n', 'Prerequisite Charms', ': None', "\nThe eyes of the Solar Exalted see the hidden truths of others’ pains. This Charm lets the Solar automatically determine which of the target’s observable traits and described symptoms are medically related. If the Solar uses this Charm in the process of a formal diagnosis, normally a dramatic (Perception + Medicine) action with a Speed of 5 long ticks, this Charm protects her from any error in diagnosis. If she has enough information, she accurately identifies each condition, its source and its additional effect. If she does not have enough information, as when a target who caught an unknown disease from eating infected human brains successfully conceals his cannibalism, she recognizes that some key piece of the puzzle is missing. As normal for diagnostics, it isn't limited to purely physiological or anatomical information; mental and spiritual information (i.e. derangements and virtues) are also valid. Having Virtues with a rating of 1 is considered madness, as does being in the throes of Limit Break. With enough information, he can even determine the target's Virtue Flaw.", 'Cost', ': -; ', 'Mins', ': Medicine 3, Essence 2;', '\n', 'Type', ': Permanent', '\n', 'Keywords', ': Mirror (Plague-Eating Kiss)', '\n', 'Duration', ': Permanent', '\n', 'Prerequisite Charms', ': Flawless Diagnosis Technique', '\nDisease and corruption cannot stand against the Solars’ healing light. Solar Exalted with this Charm can cure any Sickness effect. This Charm guarantees that any attempt Solars make to treat a sickness is considered supernatural. It halves the length of the patient’s convalescence. If the Exalt’s player rolls five or more successes on a Medicine roll for the Solar to treat an ordinarily incurable illness, such as the Great Contagion, she can spend five motes and banish it from the patient’s system. Treating sickness in this fashion is a dramatic Medicine-based action that takes one hour unless sped by a stunt or Charm.', 'Cost', ': -; ', 'Mins', ': Medicine 3, Essence 2;', '\n', 'Type', ': Permanent', '\n', 'Keywords', ': Mirror (Venom-Bleeding Agony)', '\n', 'Duration', ': Permanent', '\n', 'Prerequisite Charms', ': Flawless Diagnosis Technique', '\nThe Lawgivers bring purgation and purity. Solar Exalted with this Charm can force even the most terrible Poison effects from the target’s body. This Charm guarantees that any attempt they make to treat a poison is considered supernatural. If the Exalt’s player rolls five or more successes on a Medicine roll for the Solar to treat an ordinarily incurable poison, such as spiritual taint, Yozi impregnation, or even spells such as Blood of Boiling Oil, she can spend five motes and banish it from the patient’s system. Treating poison in this fashion is a dramatic Medicine-based action that takes 20 minutes unless sped by a stunt or Charm.', 'Cost', ': -; ', 'Mins', ': Medicine 3, Essence 2;', '\n', 'Type', ': Permanent', '\n', 'Keywords', ': Mirror (Bone Graft Technique), Obvious', '\n', 'Duration', ': Permanent', '\n', 'Prerequisite Charms',
               ': Flawless Diagnosis Technique', '\nEssence can repair even severed limbs. Solar Exalted with this Charm can cure any Crippling effect. This Charm guarantees that any attempt they make to treat the effect is considered supernatural. If the Exalt’s player rolls five or more successes on a Medicine roll for the Solar to treat an ordinarily incurable Crippling effect, such as limb amputation or Charm-induced paralysis, she can spend five motes and restore the patient. Treating Crippling injuries in this fashion is a dramatic Medicine-based action that takes one hour unless sped by a stunt or Charm.', 'Cost', ': (6 - Solar’s Essence) motes; ', 'Mins', ': Medicine 2, Essence 2;', '\n', 'Type', ': Supplemental', '\n', 'Keywords', ': None', '\n', 'Duration', ': Instant', '\n', 'Prerequisite Charms', ': Flawless Diagnosis Technique', '\nRarely is a Solar forced to leave a task unfinished. This Charm is a Medicine-based action in which the character treats a patient. The Charm functions exactly as any Medicine-based dramatic action that takes up to one hour, save that the character performs it in five normal ticks. As with Contagion-Curing Touch, the medical shortcuts involved depend on the Exalt in question. This Charm does not remove the need for appropriate medicine, surgical tools and such, but the Solar can use a stunt or Combo to work around these limitations.', '\nThis Charm speeds only that portion of treatment that actively involves the physician. It does not accelerate any rest, recovery and convalescence the patient normally performs on his own. It can act as the dramatic action required by Charms such as ', 'Wholeness-Restoring Meditation', ' and ', 'Wound-Mending Care Technique', '.', '\nAt Essence 6+ this Charm instead becomes a Permanent upgrade to the Solars’ being which requires no motes to use.', 'Cost', ': 3m per mutation point; ', 'Mins', ': Medicine 4, Essence 4;', '\n', 'Type', ': Simple (Dramatic action)', '\n', 'Keywords', ': Shaping, Stackable, Touch', '\n', 'Duration', ': Instant', '\n', 'Prerequisite Charms', ': Wholeness-Restoring Meditation', '\nThe Lawgiver need not only heal, but may recreate bodies as she sees fit. After she spends five hours performing a Medicine-based action (and making an Intelligence + Medicine roll), her target gains or loses points of physical mutations no greater than the Solar’s successes. (See ', 'Exalted', ', pp. 288-290, ', 'Manual of Exalted Power—The Lunars', ', pp. 206-209, and ', 'The Compass of Celestial Directions, Vol. II—The Wyld', ', pp. 144-148. Poxes and deficiencies are one point; afflictions/debilities, two points; blights/deformities, four points; abominations, six points.)', '\nThis Charm can remove Wyld mutations, but the mutations it grants aren’t usually of the Wyld. Unless the storyteller rules otherwise, mutations granted by this Charm don’t restrict the target’s ability to live in Creation.', 'Cost', ': -; ', 'Mins', ': Medicine 3, Essence 3;', '\n', 'Type', ': Permanent', '\n', 'Keywords', ': Native', '\n', 'Duration', ': Permanent', '\n', 'Prerequisite Charms', ': Wholeness-Restoring Meditation', '\nCreation sets a grim course for those who cycle through it. By healing others, a Solar finds the power and resolve to continue her journey. The Lawgiver regains two motes per health level restored to another character through the application of her healing arts, so long as that character’s wounds were not inflicted by the Solar or at the Solar’s behest. Once per story, the Lawgiver may waive this benefit to instead reduce her Limit by one point.', 'Cost', ': 20m, 1wp; ', 'Mins', ': Medicine 6, Essence 6;', '\n', 'Type', ': Simple', '\n', 'Keywords', ': Obvious', '\n', 'Duration', ': Instant', '\n', 'Prerequisite Charms', ': Ailment-Rectifying Method, Contagion-Curing Touch', '\nTranscending individual treatment, the Solar exercises sovereignty over disease, giving it form at her behest. The Solar selects a specific disease. All instances of the targeted disease within (Essence x 20) miles are immediately pulled from those who suffer from them, traveling at the speed of prayer to the Solar’s location. There they coalesce over the course of one day, leaping together in a roiling mass of filth and shadow that eventually becomes a single, powerful plague god of that particular disease—one which harbors an indestructible Intimacy of loyalty to the Solar who caused it to come into being. The spirit may somewhat resemble the Solar in appearance. This god is equivalent to a spirit of the second rank or third rank, depending on the virulence and magnitude of the disease and its outbreak (see ', 'The Compass of Celestial Directions, vol. III—Yu-Shan', ', pp.122-124) The spirit always has the Bane Weapon Charm, which is efficacious against other spirits of the disease it represents, and a special Charm called Consume Sickness, which allows the spirit to spend 10 motes to draw out the sickness it represents from a person and consume it, gaining a point of Willpower or restocking a Virtue channel in the process. This Charm may only function if a number of individuals of Magnitude 6 or above are infected with the disease within the targeted area.', 'Cost', ': 5m; ', 'Mins', ': Medicine 3, Essence 3;', '\n', 'Type', ': Simple (One dramatic action)', '\n', 'Keywords', ': Emotion, Merged', '\n', 'Duration', ': Instant', '\n', 'Prerequisite Charms', ': Flawless Diagnosis Technique, Touch of Blissful Release', '\nThis Charm is identical to Hastening Night’s End, but requires one hour of psychoanalysis. Removing unnatural mental influence requires an (Intelligence + Medicine) roll instead.', '\n', 'Merged', ': ', 'Hastening Night’s End', 'Cost', ': 20m, 3wp; ', 'Mins', ': Medicine 5, Essence 4;', '\n', 'Type', ': Simple (One dramatic action)', '\n', 'Keywords', ': Obvious, Shaping, Touch', '\n', 'Duration', ': Instant', '\n', 'Prerequisite Charms', ': Anointment of Miraculous Health, Wholeness-Restoring Meditation', "\nThis legendary Charm was employed only rarely in the First Age, as a reward for the most loyal of a Solar’s mortal retinue, or to preserve a favorite servant or lover. It involves a complex, delicate 12-hour medical procedure that resets the Essence flows of the target’s body and mends instabilities of the flesh. At the end of the process, the target is physically returned to the flower of youth—18 years of age for humans, or the proportional equivalent for animals. The target retains all memories and skills. This procedure is works on all living things, including Exalted, though the Celestial Exalted of the First Age weren't even aware for many thousands of years that they could die of old age. While this Charm does return a Sidereal's body to his youth, he will suddenly drop dead when he is destined to die, young or old, only more powerful magics could prevent a Sidereal of dying when they are destined to. Lunars of the Second Age, having protected themselves with Moonsilver tattoos, cannot be shaped younger with this Charm so long as that protection lasts. The target will then begin to age normally from the point of his “reset” youth."]

key_list = ['Cost', 'Mins', 'Type', 'Keywords', 'Duration', 'Prerequisite Charms', 'Cost', 'Mins', 'Type', 'Keywords', 'Duration', 'Prerequisite Charms', 'Cost', 'Mins', 'Type', 'Keywords', 'Duration', 'Prerequisite Charms', 'Cost', 'Mins', 'Type', 'Keywords', 'Duration', 'Prerequisite Charms', 'Cost', 'Mins', 'Type', 'Keywords', 'Duration', 'Prerequisite Charms', 'Cost', 'Mins', 'Type', 'Keywords', 'Duration', 'Prerequisite Charms', 'Cost', 'Mins', 'Type', 'Keywords', 'Duration', 'Prerequisite Charms', 'Cost', 'Mins', 'Type', 'Keywords', 'Duration', 'Prerequisite Charms', 'Cost', 'Mins', 'Type', 'Keywords', 'Duration', 'Prerequisite Charms', 'Cost', 'Mins', 'Type', 'Keywords', 'Duration', 'Prerequisite Charms', 'Cost', 'Mins', 'Type', 'Keywords', 'Duration', 'Prerequisite Charms', 'Cost', 'Mins', 'Type', 'Keywords', 'Duration', 'Prerequisite Charms', 'Cost', 'Mins',
            'Type', 'Keywords', 'Duration', 'Prerequisite Charms', 'Cost', 'Mins', 'Type', 'Keywords', 'Duration', 'Prerequisite Charms', 'Cost', 'Mins', 'Type', 'Keywords', 'Duration', 'Prerequisite Charms', 'Mins', 'Type', 'Keywords', 'Duration', 'Prerequisite Charms', 'Cost', 'Mins', 'Type', 'Keywords', 'Duration', 'Prerequisite Charms', 'Exalted', 'Cost', 'Mins', 'Type', 'Keywords', 'Duration', 'Prerequisite Charms', 'Mins', 'Type', 'Keywords', 'Duration', 'Prerequisite Charms', 'Cost', 'Mins', 'Type', 'Keywords', 'Duration', 'Prerequisite Charms', 'Cost', 'Mins', 'Type', 'Keywords', 'Duration', 'Prerequisite Charms', 'Cost', 'Mins', 'Type', 'Keywords', 'Duration', 'Prerequisite Charms', 'Compassion', 'Conviction', 'Temperance', 'Valor', 'Cost', 'Mins', 'Type', 'Keywords', 'Duration', 'Prerequisite Charms', 'Cost', 'Mins', 'Type', 'Keywords', 'Duration', 'Prerequisite Charms']

list_of_titles = ['Touch of Blissful Release', 'Contagion-Curing Touch', 'Wound-Mending Care Technique', 'Anointment of Miraculous Health', 'Wound-Cleansing Meditation', 'Flawless Diagnosis Technique', 'Ailment-Rectifying Method',
                  'Body-Purifying Admonitions', 'Wholeness-Restoring Meditation', 'Instant Treatment Methodology', 'Science of Mutation', 'Miracle Worker’s Redemption', 'A Hood on Death', 'Mind-Soothing Anodyne', 'Youth-Restoring Benison']

url = "http://exalted275e.wikidot.com/solar-medicine"
charm_type = url.split("/")[-1]
charm_type = charm_type.split("-")
if len(charm_type) > 2:
    exalt_type = charm_type.pop(0)
    charm_type = ' '.join(charm_type)
    charm_type = [exalt_type, charm_type]

# print(charm_type)

true_keys = []

for key in key_list:
    if key in true_keys:
        break
    else:
        true_keys.append(key)

for item in charms_list:
    if item in true_keys:
        charms_list.pop(charms_list.index(item))

# pprint.pprint(charms_list)

true_keys.append("Description")

for index, item in enumerate(charms_list):
    if item == '\n':
        charms_list.pop(charms_list.index(item))

    if re.search("^Cost:", item):
        charms_list[index] = ": -; "

cost_list = []
pattern1 = "^:.*\d+m"
pattern2 = "^:.*\d+wp"
pattern3 = ':\s*[-—];\s'
pattern4 = '^:.*motes'

# pprint.pprint(charms_list)

for text in charms_list:
    if re.search(pattern1, text) or re.match(pattern3, text) or re.search(pattern2, text) or re.search(pattern4, text):
        cost_list.append(text)

# pprint.pprint(cost_list)

list_of_list = []
append_list = []

for index_text, text in enumerate(charms_list):
    if text in cost_list:
        if not append_list:
            append_list.append(text)
        else:
            list_of_list.append(append_list)
            append_list = []
            append_list.append(text)
    else:
        append_list.append(text)

    if index_text == len(charms_list)-1:
        list_of_list.append(append_list)

# pprint.pprint(list_of_list)

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

# pprint.pprint(list_of_list)

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

# pprint.pprint(all_charms)

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
                value_dict.update({
                    part_list[0]: int(part_list[1])
                })
            value = value_dict

        if key == "Keywords" or key == "Prerequisite Charms":
            value = value.split(", ")

        charm_object[key] = value

pprint.pprint(all_charms)
