acl_num = int(input("Introduzca el número de ACL IPv4: "))

if (acl_num >= 1 and acl_num <= 99) or (acl_num >= 1300 and acl_num <= 1999):
    print(f"La ACL {acl_num} es una ACL Estándar.")
elif (acl_num >= 100 and acl_num <= 199) or (acl_num >= 2000 and acl_num <= 2699):
    print(f"La ACL {acl_num} es una ACL Extendida.")
else:
    print(f"El número {acl_num} no corresponde a una lista de acceso.")