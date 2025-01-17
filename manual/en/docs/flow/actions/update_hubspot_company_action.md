# Update company from HubSpot plugin

This plugin updates a company from HubSpot, based on provided data.

## Input
This plugin takes any payload as input.

## Outputs
This plugin returns response from HubSpot API on port **response**, or optional
error info on port **error** if one occurs.

## HubSpot app
Firstly, you need to [create an app](https://legacydocs.hubspot.com/docs/faq/how-do-i-create-an-app-in-hubspot) in 
a HubSpot developer account.

### Initiating OAuth 2.0 connection
This plugin uses OAuth 2.0, so you need to initiate an OAuth connection between your app and HubSpot.

To do that, you have to go to app auth in the HubSpot website. Below there is a path from main page to 
this:

hubspot.com -> login -> choose your account -> app menu -> choose app -> auth 

There are your client ID and client secret and here you need to define your redirect url and scopes:

* redirect URL is a URL visitors will be redirected to after granting access to your app. Please note: For 
  security reasons, this URL must use https in production. When testing using localhost, http can be used. 
  Also, you must use a domain, as IP addresses are not supported.
  
scopes: for updating company, you need to choose crm.objects.companies.write scope, but this match only with this 
  and Add Company to HubSpot plugin. For other plugins connecting to HubSpot, you should choose other scopes.
  We recommend choose all the following scopes: 
  
        crm.objects.companies.write, crm.objects.companies.read, crm.objects.contacts.write, crm.schemas.contacts.read, content

After filling the fields, copy link and open this. After that, choose the account that match the app you want to
connect with HubSpot and press the button. You'll be asked for granting access to your app, then be redirected to 
site which URL is based on the redirect URL you've defined. 

In the last site URL, there is a code you can use later.


## Plugin configuration

#### With form
* HubSpot resource - please select your HubSpot resource. It should contain: 
    * client id - the client ID of your app. You can find this in your app auth (on the HubSpot 
      website, after authentication - app menu -> choose app -> auth)
    * client secret - the client secret of your app. This also is in your app auth.
  
  Optionally:
    * if you **have** got access token:
      * refresh token - the refresh token obtained when initially authenticating your OAuth integration.
    * if you **haven't** got token:
      * redirect url - the redirect URL that was used when the user authorized your app. This must exactly match 
        the redirect_url used when initiating the OAuth 2.0 connection.
      * code - the code parameter returned to your redirect UR when the user authorized your app.
* is token got - please select true if you've got access token.
* company id - id of a company you want to update.
* properties - you can add properties for your contact. Remember to use field aliases from HubSpot.

#### JSON configuration - example

```json
{
  "source": {
    "client_id": "<your-client-id>",
    "client_secret": "<your-client-secret>",
    "refresh_token": "<your-refresh-token-optionally>",
    "access_token": "<your-access-token-optionally>",
    "redirect_url": "<your-redirect-url-optionally>",
    "code": "<your-code-optionally-optionally>"
  },
  "is_token_got": false,
  "company_id": "<your-company-id>",
  "properties":
    {
      "name": "<a-company-name>",
      "description": "<a-company-description>"
    }
}
```
