profile_name_xpath = "//h1[@dir='auto']"
profile_bio_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/span[1]"

profil = "//a//img"  # elements

i = 1
post_liker1 = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div["+str(i)+"]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/*[local-name()='svg'][1]/*[name()='g'][1]/*[name()='circle'][1]"

data1 = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div["+str(i)+"]/div/div/div[2]/div[1]"

all_react_out = "//span[@class='pcp91wgn']"  # element

all_react = "//span[contains(text(),'All')]"  # elements

about = "//span[normalize-space()='About']"

mfb_all_react_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/a[1]/div[1]/div[1]"

mfb_liker_xpath = "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div["+str(i)+"]/div[1]/div[1]/a[1]/i[1]"




work_data_xpath = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[2]/div[1]"
edu_data_xpath = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]"
current_city_data_xpath = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]"
from_city_data_xpath = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[4]/div/div/div[2]/div[1]"
relationship_data_xpath = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[5]/div/div/div[2]/div[1]"
contact_info_xpath = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[6]/div/div/div[2]/div[1]"






#
#
#
#
# news feed
# /html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[4]/section[1]/article[5]/footer[1]/div[2]/span[1]/a[1]
# /html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[4]/section[1]/article[6]/footer[1]/div[2]/span[1]/a[1]
# /html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[4]/section[1]/article[8]/footer[1]/div[2]/span[1]/a[1]
#
# gruop
# "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/section[1]/article["+1+"]/footer[1]/div[2]/span[1]/a[1]"
# /html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/section[1]/article[1]/footer[1]/div[2]/span[1]/a[1]
# /html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/section[1]/article[2]/footer[1]/div[2]/span[1]/a[1]
# /html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/section[1]/article[3]/footer[1]/div[2]/span[1]/a[1]
# /html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/section[1]/article[4]/footer[1]/div[2]/span[1]/a[1]
# /html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/section[1]/article[3]/footer[1]/div[2]/span[1]/a[1]
# /html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/section[1]/article[1]/footer[1]/div[2]/span[1]/a[1]
#
# /html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/section[1]/article[1]/footer[1]/div[2]/span[1]/a[1]
# /html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/section[1]/article[1]/footer[1]/div[2]/span[1]/a[1]
#
# privet gruop
# /html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/section[1]/section[1]/article[1]/footer[1]/div[2]/span[1]/a[1]
# /html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/section[1]/section[1]/article[1]/footer[1]/div[2]/span[1]/a[1]
# /html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/section[1]/article[1]/footer[1]/div[2]/span[1]/a[1]
# /html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/section[1]/article[4]/footer[1]/div[2]/span[1]/a[1]
# /html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/section[1]/article[7]/footer[1]/div[2]/span[1]/a[1]
# /html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/section[1]/article[6]/footer[1]/div[2]/span[1]/a[1]
#
#
# see more
# //span[normalize-space()='See More Posts']
#
# likers
#
# /html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/a[1]/div[1]
# /html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/a[1]/div[1]
# /html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/a[1]/div[1]
#
#
#
#
#
#
#
#
#
#
#
#
# /html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/section[1]/article[1]/footer[1]/div[2]/span[1]/a[1]
# /html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/section[1]/article[1]/footer[1]/div[2]/span[1]/a[1]
#
#

