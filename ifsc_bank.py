# -*- coding: utf-8 -*-

from fuzzywuzzy import process
import pandas as pd

# Source of CSV file: https://github.com/razorpay/ifsc/releases/tag/1.4.9
df1 = pd.read_csv('IFSC.csv', delimiter=',', index_col=False,) #encoding="ISO-8859–1")


def bank_branch_search(bank_query: str, branch_query: str):
    """

    :param bank_query: Bank string. Example: "icici", "hdfc bank"
    :param branch_query: Branch address string. Example:
    :return: DF row/object of the matching branch with IFSC & MICR code

    Step1: Load CSV to a DF
    Step2: Slice the results to the substring i.e. bank_string
    Step3:
        3.1) Fuzzy search the BRANCH col. with branch_query. BRANCH_NAME
        3.2) Fuzzy search the ADDRESS col. with branch_query. ADDRESS
        3.3) Compare the fuzzy search score of 3.1 and 3.2. If both scores are equal or BRANCH_NAME > ADDRESS,
            we assume the BRANCH_NAME row to be returned else ADDRESS row.

    Order of CSV Headers: ['IFSC', 'BRANCH', 'CENTRE', 'DISTRICT', 'STATE', 'ADDRESS', 'CONTACT',
           'IMPS', 'RTGS', 'CITY', 'NEFT', 'MICR']

    """

    # Step 1: Find the branch from `BANK` column
    # bank_dict = process.extractBests('ICIC', df1.BANK.to_dict(), score_cutoff=90, limit=None)
    # bank_branches = df1.loc[[l[2] for l in bank_dict]]
    # OR =>
    # PS: The following will fail if the bank name provided exceeds the bank name we have
    bank_branches = df1[df1['BANK'].str.lower().str.contains(bank_query.lower())]

    print('===== ALL BRANCHES OF BANK ======'.center(10))
    print(bank_branches)

    # FYI to convert whole column to lower case: bank_branches.ADDRESS.str.lower()
    branch_matches = process.extractBests(branch_query, bank_branches.BRANCH.to_dict())  # , limit=2)
    address_matches = process.extractBests(branch_query, bank_branches.ADDRESS.to_dict())

    best_branch = branch_matches[0]
    best_address = address_matches[0]

    print(best_address, best_branch)
    if best_branch[1] == best_address[1]:
        optimal_result = best_branch
    elif best_branch[1] > best_address[1]:
        optimal_result = best_branch
    else:
        optimal_result = best_address

    result_index = optimal_result[2]

    result_row = bank_branches.loc[result_index]

    print('==== Queried BRANCH ===='.center(10))
    print(result_row)
    return result_row

#
# _Q_BANK_ = 'bank of baroda'
# _Q_BRANCH_ = 'KALWAR ROAD, RAJASTHAN'
#
# bank_branch_search(_Q_BANK_, _Q_BRANCH_)
