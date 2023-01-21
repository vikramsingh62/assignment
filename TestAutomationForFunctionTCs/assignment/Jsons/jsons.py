#To create new user

new_user = {
    "name": "Vikram",
    "email": "vikramQA@banking.com",
    "DoB": "29/07/1991"
}
# get balance payload jsons

valid_user = {'account_number': 123456789
              }

invalid_user = {'account_number': 456456456
                }

# payloads for sending money

send_valid_user = {
    'amount': 1000,
    'self_account_number': 123456789,
    'other_account_number': 987654321
}

send_to_invalid_user = {
    'amount': 1000,
    'self_account_number': 123456789,
    'other_account_number': 456456456
}

send_exceeding_current_balance = {
    'amount': 100000,
    'self_account_number': 123456789,
    'other_account_number': 987654321
}

# payloads for withdrawing money
withdraw_valid_user= {
            'amount': 1000,
            'account_number': 123456789
        }

withdraw_invalid_user= {
            'amount': 1000,
            'account_number': 456456456
        }
withdraw_exceeding_current_balance= {
            'amount': 100000,
            'account_number': 123456789
        }

#Payloads for depositing money

deposit_payload_1 = {
            'amount': 1000,
            'account_number': 987654321
        }

deposit_payload_2 = {
            'amount': 100000,
            'account_number': 987654321
        }


correct_deposit = {
            'amount': 1000,
            'account_number': 987654321
        }