import os
import json
import datetime
from util.settings import Settings
from .util import check_folder


class Datasaver:
    def save_profile_json(username, information):
        output_file = Settings.profile_location + "/" + username
        check_folder(output_file)
        if (Settings.profile_file_with_timestamp):
            file_profile = os.path.join(output_file, username + '_' + datetime.datetime.now().strftime(
                "%Y-%m-%d %H-%M-%S") + '.json')
        else:
            file_profile = os.path.join(output_file, username + '.json')

        with open(file_profile, 'w') as fp:
            fp.write(json.dumps(information, indent=4))

    def save_profile_commenters_txt(username, user_commented_list):
        output_file = Settings.profile_location + "/" + username
        check_folder(output_file)
        if (Settings.profile_commentors_file_with_timestamp):
            file_commenters = os.path.join(output_file,
                                           username + "_commenters_" + datetime.datetime.now().strftime(
                                               "%Y-%m-%d %H-%M-%S") + ".txt")
        else:
            file_commenters = os.path.join(output_file, username + "_commenters.txt")

        print(file_commenters)
        with open(file_commenters, 'w') as fc:
            for line in user_commented_list:
                fc.write(line)
                fc.write("\n")
        fc.close()
