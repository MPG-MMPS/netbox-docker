from netbox.authentication import Group


class AuthFailed(Exception):
    pass


def add_groups(response, user, backend, *args, **kwargs):
    try:
        groups = response['groups']
    except KeyError:
        pass

    # Add all groups from oAuth token
    for group in groups:
        group, created = Group.objects.get_or_create(name=group)
        user.groups.add(group)


def remove_groups(response, user, backend, *args, **kwargs):
    try:
        groups = response['groups']
    except KeyError:
        # Remove all groups if no groups in oAuth token
        user.groups.clear()
        pass

    # Get all groups of user
    user_groups = [item.name for item in user.groups.all()]
    # Get groups of user which are not part of oAuth token
    delete_groups = list(set(user_groups) - set(groups))

    # Delete non oAuth token groups
    for delete_group in delete_groups:
        group = Group.objects.get(name=delete_group)
        user.groups.remove(group)


def set_roles(response, user, backend, *args, **kwargs):
    # Remove Roles temporary
    user.is_superuser = False
    user.is_staff = False
    try:
        groups = response['groups']
    except KeyError:
        # When no groups are set
        # save the user without Roles
        user.save()
        pass

    # Maps OIDC groups to superuser / staff role
    user.is_superuser = True if 'netbox-admin' in groups else False
    user.is_staff = True if 'netbox-user' in groups else False
    user.save()
