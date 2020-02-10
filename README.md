# Python - Make Outbound Call Tutorial

This project serves as a guide to help you build an application with FreeClimb. View this tutorial on [FreeClimb.com](https://docs.freeclimb.com/docs). Specifically, the project will:

- Make an outbound call to a specified number

## Setting up your new app within your FreeClimb account

To get started using a FreeClimb account, follow the instructions [here](https://docs.freeclimb.com/docs/getting-started-with-freeclimb).

## Setting up the Tutorial

1. Make sure you have Python 2.7.0 or later

2. Install the required packages

    ```bash
    pip install -r requirements.txt
    ```

3. Configure environment variables

   | ENV VARIABLE            | DESCRIPTION                                                                                                                                                                             |
   | ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | ACCOUNT_ID              | Account ID which can be found under [API Keys](https://www.freeclimb.com/dashboard/portal/account/authentication) in Dashboard                                                         |
   | AUTH_TOKEN              | Authentication Token which can be found under [API Keys](https://www.freeclimb.com/dashboard/portal/account/authentication) in Dashboard                                               |

4. Change variables to reflect the numbers and application in your account which you will be using in the tutorial

| ENV VARIABLE            | DESCRIPTION                                                                                                                                                                             |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| YOUR_FREECLIMB_NUMBER | Phone number which will be making the outbound call. Must be a [FreeClimb number](https://www.freeclimb.com/dashboard/portal/numbers) registered to your account.
| YOUR_VERIFIED_NUMBER | Phone number which will receive the call. Phone number must be [verified with FreeClimb](https://www.freeclimb.com/dashboard/portal/numbers/verified) while your account is in **Trial Mode**.
| YOUR_APP_ID | FreeClimb application within your account that has the 'CALL CONNECT URL' configured to your outbound call application.

## Running the Tutorial

```bash
env FLASK_APP=python_make_outbound_call_tutorial.py flask run
```
