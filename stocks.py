
def stock_purchases():
    Amazon = 3000
    Apple = 100
    Facebook = 250
    Google = 1400
    Microsoft = 200

    # Given the prices above and a client's investment budget, how much stock can they buy?
    # 1.1 TODO: Ask the client's name (use the string: "What is your name? ") and save it into a variable
    name = input ('What is your name? ')
    # 1.2 TODO: Ask the client how many dollars they would like to invest (use the string: "How much would you like to invest? $")
    # and save it into a variable
    # NOTE: When you use the `input` function to get user input, what do numbers get saved as?
    savings = float( input ('How much would you like to invest? $' ))
    # 1.3 TODO: Uncomment the line below to ask the client which stock they're interested in.
    # NOTE: Take a look at how this input string prints out
    stock =  ( input("\nWhich stock are you interested in? Enter the full name:\nAmazon\nApple\nFacebook\nGoogle\nMicrosoft\nStock Name: "))

    # Now that you have all of the client info, you can check how much they can purchase of the stock
    # they're interested in.

    # 1.4 TODO: Use `if/elif/else` conditional logic to determine how much stock the client can buy,
    # and save it in a variable
    
    # 1.5 TODO: Once you've calculated the number of stocks that can be purchased,
    # Use an f-string to print the result for the client, ala:
    # Alex has $5000 in savings and can buy 50 shares of Apple at the current price of $100.
    if savings < 100:
        print('You do not have enough to invest right now.')
    elif stock == 'Amazon' :
        shares = savings / Amazon
    elif stock == 'Apple' :
        shares = savings / Apple
    elif stock == 'Facebook' :
        shares = savings / Facebook 
    elif stock == 'Google' :
        shares = savings / Google
    elif stock == 'Microsoft' :
        shares = savings / Microsoft
    print(f'{name} has {savings} and can buy {shares} of {stock} at the current price of ${stock}.')  



# stock_purchases()


