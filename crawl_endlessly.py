from instagram_profilecrawl.crawl_profile import main as crawl_profile
import random
from util.settings import Settings

famous_starter = "instagram"
profiles_crawl_cycle = []


def randomize_numbers(amount, max_number):
    randomize_set = set()
    while len(randomize_set) < amount:
        r = random.randint(1, max_number + 1)
        randomize_set.add(r)
    return list(randomize_set)


def enter_commenters_to_stack(subject, commenters_num_to_crawl=800):
    commenters_file_name = "./instagram_profilecrawl/profiles/{}/{}_commenters.txt".format(subject,
                                                                                           subject)
    with open(commenters_file_name) as commenters_file:
        commmenters_list = commenters_file.readlines()
        commmenters_list = [x.strip() for x in commmenters_list]

        commenters_to_crawl = min(commenters_num_to_crawl, len(commmenters_list))
        randomized_indexes_of_commenters = randomize_numbers(commenters_to_crawl, len(commmenters_list))

        for index in randomized_indexes_of_commenters:
            user = commmenters_list[index - 1]
            profiles_crawl_cycle.append(user)


# taking 25 posts from instagram
Settings.limit_amount = 1
crawl_profile([famous_starter])
enter_commenters_to_stack(famous_starter, commenters_num_to_crawl=800)

# taking at most 50 posts from each user
Settings.limit_amount = 50
crawl_profile(profiles_crawl_cycle)
