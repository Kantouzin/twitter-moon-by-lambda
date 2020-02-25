from profile_manager import ProfileManager


def lambda_handler(event, context):
    ProfileManager().update_moon()
