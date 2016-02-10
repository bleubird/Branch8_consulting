import re
import numpy as np

clean_ids = []

def clean_user_ids(mongo_user_ids):
        for i in np.arange(len(mongo_user_ids)):
            id_pattern   = "(\d.......................)"
            match        = re.search(id_pattern, mongo_user_ids[i])
            text_removed = mongo_user_ids[i][match.start():match.end()]

            clean_ids.append(text_removed)
        return clean_ids
