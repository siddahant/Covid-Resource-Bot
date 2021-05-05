from database import database
from cities import cities
from resource import res1



def start(message):
    global out
    message = str(message)
    message = message.casefold()

    lis = message.split()
    for i in range(len(lis)):
        if lis[i] == "bed":
            lis[i] = 'beds'

    reslis1 = res1()
    reslis = [x.lower() for x in reslis1]
    gretting = ['hii', 'hi', 'hello', 'hey', 'hey!', "hiii"]
    blood_group = ["a-", "a+", "ab-", "ab+", "o+", "b+", "b-", "o-"]
    other = ["help", "help!", "about"]
    plas_format = [lis[0], "plasma"]
    cities_list = cities()
    city_str=""
    robot = "\U0001F916"



    for c in cities_list:
        city_str="✅ *"+str(c).capitalize()+"*\n" + city_str


    for val in lis:
        if val in (reslis + gretting):
            for x in lis:
                for y in gretting:
                    if x == y:
                        out = "Hello!🙌\n" \
                              "I'm Covid-19 Resource Bot. " + robot+ "\n" \
                              "\n" \
                              "I work across communities to help 🤝 connect relevant member based on *Covid related requirements.*⚕\n" \
                              "\n" \
                              "So please tell me what are you looking for and where❓\n\n" \
                              "Kindly answer in the given format👉(*Resource and location*) for better communication! \n\n" \
                              "Currently we are covering 🇮🇳:\n" + city_str + "\n\n🟢Example texts👇 \n💠 *Oxygen in Indore*,\n" \
                              "💠 *O+ plasma required in Mumbai*,\n" \
                              "💠 *Need oxygen cylinder in Delhi*,\n" \
                              "💠 *Required beds in Pune*, _etc.._\n" \
                              "\n" \
                              "\n" \
                              "To know more please type *help* " \
                              "and for about us please type *about*\n" \
                              "\n" \
                              "🔴 *IMPORTANT* 🔴\n" \
                              "🙏In case you have any verified contacts and would like you join us please fill the details here:\n" \
                              "Link\n" \
                              "\n" \
                              "🙏 _Every single verified leads you shared can help many people lives_ 🙏"
                        break

            for x in lis:
                for res in reslis:
                    if x == res:
                        for x in lis:
                            for city in cities_list:
                                if x == city:
                                     if res != "plasma":
                                        res = res.capitalize()
                                        fdata = database(res, city=city)
                                        if fdata.empty != True:
                                            name = [names for names in fdata['name']]
                                            contact_number = [contact_number for contact_number in fdata['contact_number']]
                                            last_varified = [last_varified for last_varified in fdata['last_verified']]
                                            links=[link for link in fdata["url"]]
                                            output1 = ""
                                            idx = 1

                                            for n, c, l,u in zip(name, contact_number, last_varified,links):
                                                output1 = "✅" + str(n).capitalize() + ": " + str(c) + '\n  ' + str(u) + "\n  (_last verified: " + str(l) + "_)\n\n" + output1
                                                idx = idx + 1
                                            pr = "🟢Some " + res + " resources are available in *" + city + "* please call📞 or message📄 to respective person:\n\n" + output1

                                            out = pr
                                            break

                                        else:
                                            out = "I'm so sorry😥, I was unable to find anyone in *"+ city+"* for *" +res+"* " \
                                                  "This is may because either I don't known several people from your city" \
                                                  "or due to high demand of *"+res+"*\n\nTo know more please type *help*"
                                            break
                                     else:
                                        if lis[0:2] == plas_format[0:2]:
                                            if lis[0] in blood_group:
                                                res = res.capitalize()
                                                basedata = database(res, city, lis[0].capitalize())
                                                if basedata.empty != True:
                                                    filter_base = basedata
                                                    name = [names for names in filter_base['name']]
                                                    contact_number = [contact_number for contact_number in
                                                                      filter_base['contact_number']]

                                                    blood = [blood for blood in filter_base["blood_group"]]
                                                    last_varified1 = [last_varified for last_varified in
                                                                      filter_base['last_verified']]
                                                    links = [link for link in filter_base["url"]]
                                                    output = ""
                                                    idx = 1
                                                    for n, c, b, l,u in zip(name, contact_number, blood, last_varified1,links):
                                                        output = "✅" + str(n) + " " + str(c) + '\n  ' + str(u) + "\n  (_last verified: " + str(l) + "_)\n\n" + output
                                                        idx = idx + 1

                                                    pr1 = "🟢"+lis[0].capitalize() + " plasma is " + "available please contact📲:\n\n" + output

                                                    out = pr1
                                                    break
                                                else:
                                                    out = "I'm so sorry😥, I was unable to find anyone in *"+ city+"* for *" +lis[0].capitalize()+" plasma* " \
                                                  "This is may because either I don't known several people from your city"\
                                                  "or due to high demand of *"+res+"*\n\nTo know more please type *help*"
                                                    break
                                            else:
                                                out = "Sorry for the inconvenience😥,\n but I was not able to find *" + lis[0].capitalize() + " blood group.*\n\nCould you please check your given blood group❓ "
                                                break

                                        else:
                                            out = "🟢For plasma please answer in the given format👉 *Blood group plasma and location*\n\n" \
                                                  "🙏please understand blood group in necessary for Plasma🙏\n\n" \
                                                  "🟢you may say:\n💠 *B+ plasma in indore*\n" \
                                                  "💠 *O+ plasma required in mumbai*\netc.."
                                            break
                            else:
                                out = "I'm so sorry😥, I was unable to find it. " \
                                      "This is may because either I don't known several people from your city, " \
                                      "or you haven't enter location correctly\n\n\n" \
                                      "Please consider changing your request❓\n" \
                                      "Make sure you have added the location correctly\n\n" \
                                      "🟢Example\n 💠*Oxygen in Indore*,\n" \
                                      "💠 *O+ plasma required in Mumbai*,\n" \
                                      "💠 *Need ambulance in Delhi*,\n" \
                                      "💠 *Required beds in Pune* _etc.._" \
                                      "\n\n" \
                                      "🟢Currently we are covering 🇮🇳:\n"+city_str+"\n\n*Hope we will covre your location soon.*🤞\n\n🟢To know more please type *help*"
                                continue
                            break
            break
        elif val == 'help' or val == 'help!':

            out = "Sure! I can help you to connect with people to help with specific *Covid-19* resources ⚕\n\n" \
                  "Please be do not panic🥶 I'm here to assist you with some relevant resources in this distressful time🤞:\n\n" \
                  "🟢Resources avaliable:\n" \
                  "💠  *Oxygen*\n" \
                  "💠  *Beds*\n" \
                  "💠  *Plasma*\n" \
                  "💠  *Ambulance*\n" \
                  "💠 *Hospital*\n" \
                  "💠  *Helpline*\n\n" \
                  "🟢Currently we are covering🇮🇳\n"+city_str+"\n" \
                  "Suppose you need some leads in your area, please answer in the given format👉 (*Resource name and location*) for better communication\n" \
                  "\n🟢Examples\n💠 *Oxygen in Indore*,\n" \
                  "💠 *O+ plasma required in Mumbai*,\n" \
                  "💠 *Need Ambulance in Delhi*,\n" \
                  "💠 *Required beds in Pune*, _etc._\n\n" \
                  "🙏 If you know any resource which is available in Indore please go to fill the details here\n" \
                  "link\n\n" \
                  "To know more about us please say about"

        elif val == "about":
            out = "about us"

        else:
            out = "I'm so sorry😥, I wasn't able to find anyone." \
                  "Please consider changing your request❓\n\n" \
                  "Make sure your spelling the resource and location correctly\n\n" \
                  "🟢Example\n 💠 *Oxygen in Indore*,\n" \
                  "💠 *O+ plasma required in Mumbai*,\n" \
                  "💠 *Need oxygen cylinder in Delhi*,\n" \
                  "💠 *Required beds in Pune* _etc._" \
                  "\n\n" \
                  "To know more please type *help*"

    return out

#
# x = start("hi")
# print(x)
