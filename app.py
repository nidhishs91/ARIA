import sentry_sdk

sentry_sdk.init(
    dsn="https://8cdc5231e8aef63d2fd7dd94d5f4ea71@o4511369733603328.ingest.us.sentry.io/4511369780527104"
)

def trigger_error():
    return 10 / 0  # intentional error

trigger_error()
