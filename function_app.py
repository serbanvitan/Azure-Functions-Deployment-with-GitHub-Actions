import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="simple_greeting")
@app.route(route="greet")  # This makes the function available at /api/greet
def greet(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(
        "Hello, world! This is a simple Azure Function.",
        status_code=200
    )
