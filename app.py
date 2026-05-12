# import sentry_sdk

# sentry_sdk.init(
#     dsn="https://8cdc5231e8aef63d2fd7dd94d5f4ea71@o4511369733603328.ingest.us.sentry.io/4511369780527104"
# )

# def trigger_error():
#     return 10 / 0  # intentional error

# trigger_error()

import sentry_sdk

sentry_sdk.init(
    dsn="https://8cdc5231e8aef63d2fd7dd94d5f4ea71@o4511369733603328.ingest.us.sentry.io/4511369780527104",
    traces_sample_rate=1.0
)

def trigger_error():
    return 10 / 0  # intentional error

try:
    trigger_error()
except Exception as e:
    event_id = sentry_sdk.capture_exception(e)
    print("SENTRY_EVENT_ID:", event_id)
    raise
