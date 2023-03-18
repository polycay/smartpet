import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="smartpet"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE smartpet")
# mycursor.execute("create table dog_info(weight int null,unit_ID int not null,age int null,birthday date null,ID int not null auto_increment PRIMARY KEY,name varchar(45) null)")
# mycursor.execute("create index fk_dog_info_unit1_idx on dog_info (unit_ID)")
# mycursor.execute("create table dogweight_portionsize(unit_id int not null,portieanalyse_ID int not null,max_weight_dog int null,min_weight_dog int null,primary key (unit_id, portieanalyse_ID))")
# mycursor.execute("create index `fk_max_gewciht_hond_portieanalyse1_idx` on dogweight_portionsize (portieanalyse_ID)")
# mycursor.execute("create table feeding_times(ID int not null auto_increment primary key,time time null)")
# mycursor.execute("create table food_eaten(ID int not null auto_increment,portionsize decimal(10,2) not null,unit_id int not null,ball_used tinyint(1) null,timestamp timestamp default CURRENT_TIMESTAMP not null,primary key (ID, unit_id))")
# mycursor.execute("create index fk_food_eaten_unit1_idx on food_eaten (unit_id)")
# mycursor.execute("create table food_reservoir(ID int not null auto_increment,weight decimal(10,2) not null,unit_id int not null,timestamp timestamp default CURRENT_TIMESTAMP not null,primary key (ID, unit_id))")
# mycursor.execute("create index fk_food_reservoir_unit1_idx on food_reservoir (unit_id)")
# mycursor.execute("create table max_portionsize(unit_ID int not null,ID int not null auto_increment primary key,weight decimal(10,2) null,timestamp timestamp default CURRENT_TIMESTAMP not null)")
# mycursor.execute("create index fk_max_portionsize_unit1_idx on max_portionsize (unit_ID)")
# mycursor.execute("create table portieanalyse(ID int not null auto_increment,portionsize varchar(45) null,unit_id int not null,primary key (ID, unit_id))")
# mycursor.execute("create index fk_portieanalyse_unit1_idx on portieanalyse (unit_id)")
# mycursor.execute("alter table dogweight_portionsize add constraint `fk_max gewciht hond_portieanalyse1` foreign key (portieanalyse_ID) references portieanalyse (ID)")
# mycursor.execute("create table resting_portionsize(ID int not null auto_increment primary key,weight int null,unit_ID int null,timestamp timestamp default CURRENT_TIMESTAMP not null)")
# mycursor.execute("create index resting_portionsize_unit_ID_fk on resting_portionsize (unit_ID)")
# mycursor.execute("create table unit(ID int not null auto_increment primary key,unit varchar(45) null)")
# mycursor.execute("alter table dog_info add constraint fk_dog_info_unit1 foreign key (unit_ID) references unit(ID)")
# mycursor.execute("alter table dogweight_portionsize add constraint `fk_max gewciht hond_unit1` foreign key (unit_id) references unit (ID)")
# mycursor.execute("alter table food_eaten add constraint fk_food_eaten_unit1 foreign key (unit_id) references unit (ID)")
# mycursor.execute("alter table food_reservoir add constraint fk_food_reservoir_unit1 foreign key (unit_id) references unit (ID)")
# mycursor.execute("alter table max_portionsize add constraint fk_max_portionsize_unit1 foreign key (unit_ID) references unit (ID)")
# mycursor.execute("alter table portieanalyse add constraint fk_portieanalyse_unit1 foreign key (unit_id) references unit (ID)")
# mycursor.execute("alter table resting_portionsize add constraint resting_portionsize_unit_ID_fk foreign key (unit_ID) references unit (ID)")
mycursor

mydb.commit()