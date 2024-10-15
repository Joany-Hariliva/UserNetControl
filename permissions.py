import os

def get_user_permissions(username):
    if os.name == 'nt':  # Windows
        import win32security
        import win32con
        sid = win32security.LookupAccountName(None, username)[0]
        dacl = win32security.GetFileSecurity('.', win32security.DACL_SECURITY_INFORMATION).GetSecurityDescriptorDacl()
        permissions = []
        for i in range(dacl.GetAceCount()):
            ace = dacl.GetAce(i)
            if ace[2] == sid:
                permissions.append(win32security.ACCESS_ALLOWED_ACE_TYPE)
        return permissions
    else:
        return os.system(f"groups {username}")
