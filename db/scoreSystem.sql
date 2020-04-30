/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2020/4/13 ÐÇÆÚÒ» 18:43:00                       */
/*==============================================================*/


drop table if exists score;

drop table if exists student;

drop table if exists subject;

drop table if exists sys_role;

drop table if exists sys_user;

drop table if exists sys_user_role;

drop table if exists teacher;

/*==============================================================*/
/* Table: score                                                 */
/*==============================================================*/
create table score
(
   id                   int not null auto_increment,
   student_id           int,
   subject_id           int,
   value                varchar(100),
   primary key (id)
);

alter table score comment 'score';

/*==============================================================*/
/* Table: student                                               */
/*==============================================================*/
create table student
(
   id                   int not null auto_increment,
   name                 varchar(50),
   sex                  varchar(50),
   class                varchar(50),
   student_id           varchar(50),
   auth_string          varchar(255),
   pic                  varchar(255),
   phone                varchar(50),
   email                varchar(50),
   primary key (id)
);

alter table student comment 'student';

/*==============================================================*/
/* Table: subject                                               */
/*==============================================================*/
create table subject
(
   id                   int not null auto_increment,
   name                 varchar(255),
   teacher_id           int,
   student_id           int,
   primary key (id)
);

alter table subject comment 'subject';

/*==============================================================*/
/* Table: sys_role                                              */
/*==============================================================*/
create table sys_role
(
   id                   int not null auto_increment,
   name                 varchar(50),
   code                 varchar(50),
   primary key (id)
);

alter table sys_role comment 'sys_role';

/*==============================================================*/
/* Table: sys_user                                              */
/*==============================================================*/
create table sys_user
(
   id                   int not null auto_increment,
   name                 varchar(64),
   auth_string          varchar(100),
   phone                varchar(50),
   email                varchar(50),
   primary key (id)
);

alter table sys_user comment 'sys_user';

/*==============================================================*/
/* Table: sys_user_role                                         */
/*==============================================================*/
create table sys_user_role
(
   id                   int not null auto_increment,
   user_id              int,
   role_id              int,
   primary key (id)
);

alter table sys_user_role comment 'sys_user_role';

/*==============================================================*/
/* Table: teacher                                               */
/*==============================================================*/
create table teacher
(
   id                   int not null auto_increment,
   name                 varchar(50),
   auth_string          varchar(255),
   phone                varchar(50),
   job_title            varchar(100),
   pic                  varchar(255),
   email                varchar(50),
   primary key (id)
);

alter table teacher comment 'teacher';

