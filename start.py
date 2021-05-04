from database import database


def start(message):
    message = str(message)
    message = message.casefold()

    lis = message.split()
    for i in range(len(lis)):
        if lis[i] == "bed":
            lis[i] = 'beds'

    reslis = ['oxygen', 'beds', 'ambulance', "plasma"]
    gretting = ['hii', 'hi', 'hello', 'hey', 'hey!', "hiii"]
    blood_group = ["a-", "a+", "ab-", "ab+", "o+", "b+", "b-", "o-"]
    other = ["help", "help!", "about"]
    plas_format = [lis[0], "plasma"]



    for val in lis:
        if val in (reslis + gretting):
            for x in lis:
                for y in gretting:
                    if x == y:
                        out = "Hello indore!\n" \
                              "Im Indore Covid Resource Bot\n" \
                              "\n" \
                              "Please tell me what are you looking:\n" \
                              "*Oxygen*\n" \
                              "*Beds*\n" \
                              "*Plasma* (please say like that : *B+ plasma*)\n" \
                              "*Ambulance*\n" \
                              "\n"
                        break


            for x in lis:
                for res in reslis:
                    if x == res:
                        if res != "plasma":
                            res = res.capitalize()
                            fdata = database(res)
                            name = [names for names in fdata['name']]
                            contact_number = [contact_number for contact_number in fdata['contact_number']]
                            last_varified = [last_varified for last_varified in fdata['last_verified']]
                            output1 = ""

                            for n, c, l in zip(name, contact_number, last_varified):
                                output1 = str(n) + " " + str(c) + '\n' + "(_last verified_ " + str(l) + ")\n\n" + output1

                            pr = "Some " + res + " resources are available please call or go to given location:\n\n" + output1

                            out = pr
                            break

                        else:
                            if lis == plas_format:
                                if lis[0] in blood_group:
                                    basedata = database(res, lis[0].capitalize())
                                    filter_base = basedata
                                    name = [names for names in filter_base['name']]
                                    contact_number = [contact_number for contact_number in
                                                      filter_base['contact_number']]
                                    blood = [blood for blood in filter_base["blood_group"]]
                                    last_varified1 = [last_varified for last_varified in filter_base['last_verified']]
                                    output = ""
                                    for n, c, b, l in zip(name, contact_number, blood, last_varified1):
                                        output =  str(n) + " " + str(
                                            c) + '\n' + "(_last verified_ " + str(l) + ")\n\n" + output
                                    pr1= str(b) + " plasma is " + "available please contact :\n\n" + output
                                    out = pr1
                                else:
                                    out = " please check blood group"
                            else:
                                out = "please correct the plasma input format : Blood group plasma\n" \
                                      "For example: *B+ plasma*"
            break

        elif val == 'help' or val == 'help!':
            out = "Sure! I can help you to connect with people to help with specific *Covid-19* resource in *Indore*\n\n" \
                  "Please be don't panic and tell me what are you looking:\n" \
                  "*Oxygen*\n" \
                  "*Beds*\n" \
                  "*Plasma*\nplease say like that: *B+ plasma*\n" \
                  "*Ambulance*\n" \
                  "\n" \
                  "If you know any resource which is available in Indore please go to fill the details here\n" \
                  "link\n\n" \
                  "To know more about us please say about"

        elif val == "about":
            out = "about us"

        else:
            out = "Sorry for inconvenience, I'm not understand what you said\nPlease try again\nor\nTo know my capabilities please type *help*"


    return out


