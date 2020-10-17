create table user(
	user_id int,
    created_date bigint, 
    updated_date bigint,
    user_name varchar(15) unique,
    full_name varchar(50),
    image_url varchar(255),
    address varchar(100),
    mobile varchar(50),
    email varchar(50),
    password varchar(100),
    image_path varchar(200),
    status smallint,
    primary key(user_id)
);
create table food(
	food_id int,
    created_date bigint, 
    updated_date bigint,
    name varchar(50),
    init_price float,
    sale_price float,
    image varchar(255),
    title varchar(255),
    content varchar(255),
    rate_avg float,
    rate_one_star float,
	rate_two_star float,
    rate_three_star float,
    rate_four_star float,
    rate_five_star float,
	total_like int,
    store_id int,
    category_id int,
    primary key (food_id)
);
create table foodimage(
	food_image_id int,
    created_date bigint, 
    updated_date bigint,
	image varchar(255),
    food_id int,
    primary key(food_image_id)
);
create table order(
	order_id int,
    created_date bigint, 
    updated_date bigint,
    address varchar(100),
    user_id int,
    shipper_id int,
    order_status tinyint,
    primary key(order_id)
);
create table orderfood(
	order_id int,
    food_id int,
    created_date bigint, 
    updated_date bigint,
    quantity int,
    price float,
    options_orderfood tinyint,
    primary key(order_id,food_id)
);
create table store(
	store_id int,
    created_date bigint, 
    updated_date bigint,
    name varchar(255),
    primary key(store_id)
)
create table admin(
	admin_id int,
    created_date bigint, 
    updated_date bigint,
    name varchar(255),
    password varchar(255),
    username varchar(255)
    primary key(admin_id)
)
create table adminrole(
    admin_id int,
    role_id int,
    created_date bigint, 
    updated_date bigint,
    primary key(admin_id),
    primary key(role_id)
)
create table role(
    created_date bigint, 
    updated_date bigint,
    role_id int,
    name varchar(255),
    primary key(role_id)
)
create table rolepage(
    created_date bigint, 
    updated_date bigint,
    page_id int,
    role_id int,
    primary key(page_id)
    primary key(role_id)
)
create table page(
    created_date bigint, 
    updated_date bigint,
    page_id int,
    name varchar(255),
    primary key(page_id)
)

create table menu(
    created_date bigint, 
    updated_date bigint,
    menu_id int,
    name varchar(255),
    page_id int,
    is_parent tinyint
    primary key(menu_id)
)