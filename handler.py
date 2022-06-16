from profile_manager import ProfileManager


def main(event, context):
    ProfileManager().update_moon()


if __name__ == "__main__":
    main(None, None)
