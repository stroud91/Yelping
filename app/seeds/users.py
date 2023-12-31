from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demolition', email='demo@aa.io', first_name='Demo', last_name='Lition', password='password' , profile_image_id="https://robohash.org/1")
    marnie = User(
        username='marniemorine', email='marnie@aa.io', first_name='Marnie', last_name='Mornie', password='password1', profile_image_id="https://robohash.org/2")
    bobbie = User(
        username='bobbiebuild', email='bobbie@aa.io',first_name='Bobbie', last_name='Builder', password='password11', profile_image_id="https://robohash.org/3")
    nemo = User(
        username='FakeUser1', email='user1@user.io', first_name='Nemo', last_name='Dora', password='password2', profile_image_id="https://robohash.org/4")
    john_smith = User(
        username='FakeUser2', email='user2@user.io', first_name='John', last_name='Smith', password='password3', profile_image_id="https://robohash.org/5")
    john_doe = User(
        username='johndoe', email='johndoe@user.io', first_name='John', last_name='Doe', password='password4', profile_image_id="https://robohash.org/6")
    nemodon = User(
        username='nemotobefound', email='nemodoramon@user.io', first_name='Nemodon', last_name='Doramon', password='password5', profile_image_id="https://robohash.org/7")
    tobe = User(
        username='youguessedit', email='englishwriter@user.io', first_name='Tobe', last_name='Ornottobe', password='password6', profile_image_id="https://robohash.org/8")
    stu = User(
        username='studybuddy', email='hitthebooks@user.io', first_name='Stu', last_name='Dent', password='password7', profile_image_id="https://robohash.org/9")
    ali = User(
        username='seeyoulater', email='farewellgreetings@goodbyes.io', first_name='Ali', last_name='Bye', password='password8', profile_image_id="https://robohash.org/10")
    dee = User(
        username='gatekeeper', email='noboundaries@user.io', first_name='Dee', last_name='Fence', password='password9', profile_image_id="https://robohash.org/11")
    justin = User(
        username='clockwatcher', email='punctual@ontime.io', first_name='Justin', last_name='Thyme', password='password21', profile_image_id="https://robohash.org/12")
    anna_lytics = User(
        username='data_diva', email='analyse@data.io', first_name='Anna', last_name='Lytics', password='password22', profile_image_id="https://robohash.org/13")
    ella_ment = User(
        username='basics', email='foundation@core.io', first_name='Ella', last_name='Ment', password='password23', profile_image_id="https://robohash.org/14")
    sam_sung = User(
        username='smart_phone', email='galaxy@android.io', first_name='Sam', last_name='Sung', password='password24', profile_image_id="https://robohash.org/15")
    ava_cado = User(
        username='green_inside', email='healthyfats@fruit.io', first_name='Ava', last_name='Cado', password='password25', profile_image_id="https://robohash.org/16")
    ben_chmark = User(
        username='test_speed', email='perform@fast.io', first_name='Ben', last_name='Chmark', password='password26', profile_image_id="https://robohash.org/17")
    perry_scope = User(
        username='wide_view', email='lookout@sea.io', first_name='Perry', last_name='Scope', password='password27', profile_image_id="https://robohash.org/18")
    maya_rchitecture = User(
        username='build_design', email='construct@build.io', first_name='Maya', last_name='Rchitecture', password='password28', profile_image_id="https://robohash.org/19")
    artie_choke = User(
        username='veggie_love', email='healthy@veg.io', first_name='Artie', last_name='Choke', password='password29', profile_image_id="https://robohash.org/20")
    elmer_aldente = User(
        username='pasta_chef', email='italian@food.io', first_name='Elmer', last_name='Aldente', password='password30', profile_image_id="https://robohash.org/21")
    max_out = User(
        username='full_power', email='strength@lift.io', first_name='Max', last_name='Out', password='password31', profile_image_id="https://robohash.org/22")
    penny_tration = User(
        username='focused', email='detailed@precise.io', first_name='Penny', last_name='Tration', password='password32', profile_image_id="https://robohash.org/23")
    bill_ding = User(
        username='realestate_mogul', email='property@house.io', first_name='Bill', last_name='Ding', password='password33', profile_image_id="https://robohash.org/24")
    miles_ahead = User(
        username='leading', email='forward@advance.io', first_name='Miles', last_name='Ahead', password='password34', profile_image_id="https://robohash.org/25")
    sandy_beach = User(
        username='ocean_lover', email='waves@sea.io', first_name='Sandy', last_name='Beach', password='password35', profile_image_id="https://robohash.org/26")
    terra_byte = User(
        username='huge_storage', email='data@big.io', first_name='Terra', last_name='Byte', password='password36', profile_image_id="https://robohash.org/27")
    will_power = User(
        username='motivated', email='drive@success.io', first_name='Will', last_name='Power', password='password37', profile_image_id="https://robohash.org/28")
    ivan_idea = User(
        username='innovator', email='brainstorm@think.io', first_name='Ivan', last_name='Idea', password='password38', profile_image_id="https://robohash.org/29")
    luke_warm = User(
        username='not_hot', email='medium@heat.io', first_name='Luke', last_name='Warm', password='password39', profile_image_id="https://robohash.org/30")
    sue_shef = User(
        username='sushi_maker', email='japanese@food.io', first_name='Sue', last_name='Shef', password='password40', profile_image_id="https://robohash.org/31")
    dee_signer = User(
        username='aesthetic', email='creative@design.io', first_name='Dee', last_name='Signer', password='password41', profile_image_id="https://robohash.org/32")
    tim_ber = User(
        username='wood_fella', email='forestry@trees.io', first_name='Tim', last_name='Ber', password='password42', profile_image_id="https://robohash.org/33")
    elle_vate = User(
        username='rise_above', email='lift@high.io', first_name='Elle', last_name='Vate', password='password43', profile_image_id="https://robohash.org/34")
    gene_pool = User(
        username='evolutionary', email='biology@dna.io', first_name='Gene', last_name='Pool', password='password44', profile_image_id="https://robohash.org/35")
    mo_tion = User(
        username='always_moving', email='physics@speed.io', first_name='Mo', last_name='Tion', password='password45', profile_image_id="https://robohash.org/36")
    ray_diate = User(
        username='shine_bright', email='energy@glow.io', first_name='Ray', last_name='Diate', password='password46', profile_image_id="https://robohash.org/37")
    cat_tle = User(
        username='farm_lord', email='ranch@herd.io', first_name='Cat', last_name='Tle', password='password47', profile_image_id="https://robohash.org/38")
    liz_ard = User(
        username='cold_blooded', email='reptile@scale.io', first_name='Liz', last_name='Ard', password='password48', profile_image_id="https://robohash.org/39")
    bob_sleigh = User(
        username='snow_rider', email='winter@sled.io', first_name='Bob', last_name='Sleigh', password='password49', profile_image_id="https://robohash.org/40")
    colin_all = User(
        username='mass_dialer', email='phone@call.io', first_name='Colin', last_name='All', password='password50', profile_image_id="https://robohash.org/41")
    gail_force = User(
        username='windy_lady', email='weather@storm.io', first_name='Gail', last_name='Force', password='password51', profile_image_id="https://robohash.org/42")
    al_gebra = User(
        username='math_whiz', email='equations@solve.io', first_name='Al', last_name='Gebra', password='password52', profile_image_id="https://robohash.org/43")
    minnie_mum = User(
        username='least_amount', email='basic@small.io', first_name='Minnie', last_name='Mum', password='password53', profile_image_id="https://robohash.org/44")
    pat_tern = User(
        username='design_repeat', email='style@loop.io', first_name='Pat', last_name='Tern', password='password54', profile_image_id="https://robohash.org/45")
    jess_ter = User(
        username='court_joker', email='playful@funny.io', first_name='Jess', last_name='Ter', password='password55', profile_image_id="https://robohash.org/46")
    sal_mon = User(
        username='river_swimmer', email='fish@ocean.io', first_name='Sal', last_name='Mon', password='password56', profile_image_id="https://robohash.org/47")
    rob_in = User(
        username='bird_lover', email='nature@fly.io', first_name='Rob', last_name='In', password='password57', profile_image_id="https://robohash.org/48")
    grace_full = User(
        username='elegant_dancer', email='ballet@move.io', first_name='Grace', last_name='Full', password='password58', profile_image_id="https://robohash.org/49")
    brooke_lyn = User(
        username='ny_resident', email='newyork@bridge.io', first_name='Brooke', last_name='Lyn', password='password59', profile_image_id="https://robohash.org/50")
    amber_alert = User(
        username='safety_first', email='emergency@warning.io', first_name='Amber', last_name='Alert', password='password60', profile_image_id="https://robohash.org/51")
    earl_y = User(
        username='morning_person', email='dawn@rise.io', first_name='Earl', last_name='Y', password='password61', profile_image_id="https://robohash.org/52")
    mae_flower = User(
        username='pilgrim_ship', email='voyages@sea.io', first_name='Mae', last_name='Flower', password='password62', profile_image_id="https://robohash.org/53")
    will_power = User(
        username='inner_strength', email='determination@resolve.io', first_name='Will', last_name='Power', password='password63', profile_image_id="https://robohash.org/54")
    jack_pot = User(
        username='luck_winner', email='gambling@casino.io', first_name='Jack', last_name='Pot', password='password64', profile_image_id="https://robohash.org/55")
    anne_chor = User(
        username='sea_stable', email='ships@dock.io', first_name='Anne', last_name='Chor', password='password65', profile_image_id="https://robohash.org/56")
    carrie_on = User(
        username='continue_forward', email='luggage@travel.io', first_name='Carrie', last_name='On', password='password66', profile_image_id="https://robohash.org/57")
    terri_tory = User(
        username='land_owner', email='geography@maps.io', first_name='Terri', last_name='Tory', password='password67', profile_image_id="https://robohash.org/58")
    rocky_mountain = User(
        username='high_peak', email='geology@hike.io', first_name='Rocky', last_name='Mountain', password='password68', profile_image_id="https://robohash.org/59")
    sue_venir = User(
        username='travel_reminder', email='gifts@tourist.io', first_name='Sue', last_name='Venir', password='password69', profile_image_id="https://robohash.org/60")
    claire_voyant = User(
        username='future_seer', email='mystic@oracle.io', first_name='Claire', last_name='Voyant', password='password70', profile_image_id="https://robohash.org/61")
    don_ke = User(
        username='loyal_beast', email='animals@farm.io', first_name='Don', last_name='Ke', password='password71', profile_image_id="https://robohash.org/61")
    sandy_beach = User(
        username='ocean_lover', email='vacations@coast.io', first_name='Sandy', last_name='Beach', password='password72', profile_image_id="https://robohash.org/63")
    guy_dance = User(
        username='path_leader', email='mentor@advise.io', first_name='Guy', last_name='Dance', password='password73', profile_image_id="https://robohash.org/64")
    ali_mony = User(
        username='financial_support', email='divorce@payments.io', first_name='Ali', last_name='Mony', password='password74', profile_image_id="https://robohash.org/65")
    jan_uary = User(
        username='new_beginnings', email='calendar@yearstart.io', first_name='Jan', last_name='Uary', password='password75', profile_image_id="https://robohash.org/66")
    rose_garden = User(
        username='flower_enthusiast', email='botany@blooms.io', first_name='Rose', last_name='Garden', password='password76', profile_image_id="https://robohash.org/67")
    elle_ectric = User(
        username='power_charge', email='energy@spark.io', first_name='Elle', last_name='Ectric', password='password77', profile_image_id="https://robohash.org/68")
    anita_job = User(
        username='employment_seeker', email='career@work.io', first_name='Anita', last_name='Job', password='password78', profile_image_id="https://robohash.org/69")
    steve_adore = User(
        username='ocean_gate', email='shipping@harbor.io', first_name='Steve', last_name='Adore', password='password79', profile_image_id="https://robohash.org/70")
    pearl_harbor = User(
        username='historic_event', email='ww2@1941.io', first_name='Pearl', last_name='Harbor', password='password80', profile_image_id="https://robohash.org/71")
    ivan_idea = User(
        username='creative_thinker', email='innovation@brain.io', first_name='Ivan', last_name='Idea', password='password81', profile_image_id="https://robohash.org/72")
    luke_sky = User(
        username='galaxy_faraway', email='star@wars.io', first_name='Luke', last_name='Sky', password='password82', profile_image_id="https://robohash.org/73")
    bee_long = User(
        username='fit_in', email='place@home.io', first_name='Bee', last_name='Long', password='password83', profile_image_id="https://robohash.org/74")
    sam_wich = User(
        username='tasty_bite', email='food@lunch.io', first_name='Sam', last_name='Wich', password='password84', profile_image_id="https://robohash.org/75")
    rick_roll = User(
        username='never_giveup', email='music@meme.io', first_name='Rick', last_name='Roll', password='password85', profile_image_id="https://robohash.org/76")
    rob_bery = User(
        username='steal_spotlight', email='crime@catchme.io', first_name='Rob', last_name='Bery', password='password86', profile_image_id="https://robohash.org/77")
    stella_rspace = User(
        username='inter_galactic', email='astronomy@cosmos.io', first_name='Stella', last_name='Rspace', password='password87', profile_image_id="https://robohash.org/78")
    al_bert = User(
        username='scientific_genius', email='relativity@physics.io', first_name='Al', last_name='Bert', password='password88', profile_image_id="https://robohash.org/79")
    hugh_morous = User(
        username='always_joking', email='comedy@funny.io', first_name='Hugh', last_name='Morous', password='password89', profile_image_id="https://robohash.org/79")
    sue_she = User(
        username='roll_withit', email='food@japan.io', first_name='Sue', last_name='She', password='password90', profile_image_id="https://robohash.org/80")
    ted_talk = User(
        username='public_speaker', email='presentation@ideas.io', first_name='Ted', last_name='Talk', password='password91', profile_image_id="https://robohash.org/81")
    jed_i = User(
        username='force_user', email='lightsaber@rebel.io', first_name='Jed', last_name='I', password='password92', profile_image_id="https://robohash.org/82")
    ian_vent = User(
        username='air_flow', email='breath@fresh.io', first_name='Ian', last_name='Vent', password='password93', profile_image_id="https://robohash.org/83")
    frank_enstein = User(
        username='created_monster', email='science@lab.io', first_name='Frank', last_name='Enstein', password='password94', profile_image_id="https://robohash.org/84")
    ella_ment = User(
        username='basic_component', email='nature@particle.io', first_name='Ella', last_name='Ment', password='password95', profile_image_id="https://robohash.org/85")
    terry_fic = User(
        username='made_up_story', email='literature@fiction.io', first_name='Terry', last_name='Fic', password='password96', profile_image_id="https://robohash.org/86")
    bob_wire = User(
        username='keep_out', email='fence@border.io', first_name='Bob', last_name='Wire', password='password97', profile_image_id="https://robohash.org/87")
    eva_luation = User(
        username='assess_value', email='judgment@scale.io', first_name='Eva', last_name='Luation', password='password98', profile_image_id="https://robohash.org/88")
    art_ist = User(
        username='painting_genius', email='canvas@colors.io', first_name='Art', last_name='Ist', password='password99', profile_image_id="https://robohash.org/89")
    heidi_seek = User(
        username='where_amI', email='game@hidden.io', first_name='Heidi', last_name='Seek', password='password100', profile_image_id="https://robohash.org/90")
    jenny_rate = User(
        username='create_power', email='energy@machinery.io', first_name='Jenny', last_name='Rate', password='password101', profile_image_id="https://robohash.org/91")

    db.session.add_all([demo, marnie, bobbie, nemo, john_smith, john_doe, nemodon, tobe, stu, ali, dee, justin,
                        anna_lytics, ella_ment, sam_sung,
                        ava_cado, ben_chmark, perry_scope, maya_rchitecture, artie_choke, elmer_aldente,
                        max_out, penny_tration, bill_ding, miles_ahead, sandy_beach, terra_byte, will_power,
                        ivan_idea, luke_warm, sue_shef, dee_signer,tim_ber, elle_vate, gene_pool, mo_tion,
                        ray_diate, cat_tle, liz_ard, bob_sleigh, colin_all, gail_force,
                        al_gebra, minnie_mum, pat_tern, jess_ter, sal_mon, rob_in, grace_full, brooke_lyn,
                        amber_alert, earl_y,mae_flower, will_power, jack_pot, anne_chor, carrie_on,
                        terri_tory, rocky_mountain, sue_venir, claire_voyant, don_ke,
                        sandy_beach, guy_dance, ali_mony, jan_uary, rose_garden, elle_ectric,
                        anita_job, steve_adore, pearl_harbor, ivan_idea,luke_sky, bee_long, sam_wich, rick_roll, rob_bery,
                        stella_rspace, al_bert, hugh_morous, sue_she, ted_talk,
                        jed_i, ian_vent, frank_enstein, ella_ment, terry_fic,
                        bob_wire, eva_luation, art_ist, heidi_seek, jenny_rate])
    # db.session.add(demo)
    db.session.commit()



def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
