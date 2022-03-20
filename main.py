certs_names = []
CertsConfForAlteon = open(r"C:\\Users\yehudap\Desktop\CAT\cert_conf.txt", "w")

cert = open(r"C:\\Users\yehudap\Desktop\cert.crt")
cert_content = cert.read()


key = open(r"C:\\Users\yehudap\Desktop\cert.key")
key_content = key.read()

with open(r"C:\\Users\yehudap\Desktop\CAT\td_1.txt") as file:
    for line in file:
        line = line.rstrip()
        if "srvrcert cert" in line:
            cert_name = line.split("srvrcert cert ")[1]
            #print(cert_name)
            if cert_name not in certs_names:
                certs_names.append(cert_name)

for i in certs_names:
    print(i)
    CertsConfForAlteon.write("/c/slb/ssl/certs/cert " + i + "\n")
    CertsConfForAlteon.write("/c/slb/ssl/certs/import cert " + i + " text" + "\n")
    CertsConfForAlteon.write(cert_content)
    CertsConfForAlteon.write("\n")

    CertsConfForAlteon.write("/c/slb/ssl/certs/key " + i + "\n")
    CertsConfForAlteon.write("/c/slb/ssl/certs/import key " + i + " text" + "\n")
    CertsConfForAlteon.write(key_content)
    CertsConfForAlteon.write("\n")

