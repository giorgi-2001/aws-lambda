def lambda_handler(event, context):
    names: list = event.get('names', ['World'])
    all_greetings = []
    
    for name in names:
        greeting = f"Hello, {name}!"
        all_greetings.append(greeting)
        
    return {
           'statusCode': 200,
           'body': all_greetings
    }