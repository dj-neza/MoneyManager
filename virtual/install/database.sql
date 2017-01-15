BEGIN;
--
-- Create model Categories
--
CREATE TABLE "money_categories" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "cat_name" varchar(50) NOT NULL, "cat_for" integer NOT NULL);
--
-- Create model Expenses
--
CREATE TABLE "money_expenses" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "exp_name" varchar(50) NOT NULL, "exp_date" date NOT NULL, "exp_rep" integer NOT NULL, "exp_loan" bool NOT NULL, "exp_loan_to" varchar(50) NOT NULL, "cat_exp_id" integer NOT NULL REFERENCES "money_categories" ("id"));
--
-- Create model Goals
--
CREATE TABLE "money_goals" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "goal_name" varchar(50) NOT NULL, "goal_amount" integer NOT NULL, "goal_deadline" date NOT NULL, "amount_now" integer NOT NULL);
--
-- Create model Incomes
--
CREATE TABLE "money_incomes" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "inc_name" varchar(50) NOT NULL, "inc_date" date NOT NULL, "inc_rep" integer NOT NULL, "inc_debt" bool NOT NULL, "inc_debt_to" varchar(50) NOT NULL, "cat_inc_id" integer NOT NULL REFERENCES "money_categories" ("id"));
--
-- Create model Users
--
CREATE TABLE "money_users" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_name" varchar(50) NOT NULL, "e_mail" varchar(254) NOT NULL, "pass_word" varchar(100) NOT NULL, "currency" integer NOT NULL, "decimal" integer NOT NULL);
--
-- Create model Wallets
--
CREATE TABLE "money_wallets" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "wal_name" varchar(50) NOT NULL, "user_wal_id" integer NOT NULL REFERENCES "money_users" ("id"));
--
-- Add field user_inc to incomes
--
ALTER TABLE "money_incomes" RENAME TO "money_incomes__old";
CREATE TABLE "money_incomes" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "inc_name" varchar(50) NOT NULL, "inc_date" date NOT NULL, "inc_rep" integer NOT NULL, "inc_debt" bool NOT NULL, "inc_debt_to" varchar(50) NOT NULL, "cat_inc_id" integer NOT NULL REFERENCES "money_categories" ("id"), "user_inc_id" integer NOT NULL REFERENCES "money_users" ("id"));
INSERT INTO "money_incomes" ("inc_rep", "inc_debt", "cat_inc_id", "user_inc_id", "inc_name", "inc_date", "id", "inc_debt_to") SELECT "inc_rep", "inc_debt", "cat_inc_id", NULL, "inc_name", "inc_date", "id", "inc_debt_to" FROM "money_incomes__old";
DROP TABLE "money_incomes__old";
CREATE INDEX "money_expenses_e340c790" ON "money_expenses" ("cat_exp_id");
CREATE INDEX "money_wallets_97d1e71a" ON "money_wallets" ("user_wal_id");
CREATE INDEX "money_incomes_f03f3b24" ON "money_incomes" ("cat_inc_id");
CREATE INDEX "money_incomes_31bd3004" ON "money_incomes" ("user_inc_id");
--
-- Add field wal_inc to incomes
--
ALTER TABLE "money_incomes" RENAME TO "money_incomes__old";
CREATE TABLE "money_incomes" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "inc_name" varchar(50) NOT NULL, "inc_date" date NOT NULL, "inc_rep" integer NOT NULL, "inc_debt" bool NOT NULL, "inc_debt_to" varchar(50) NOT NULL, "cat_inc_id" integer NOT NULL REFERENCES "money_categories" ("id"), "user_inc_id" integer NOT NULL REFERENCES "money_users" ("id"), "wal_inc_id" integer NOT NULL REFERENCES "money_wallets" ("id"));
INSERT INTO "money_incomes" ("inc_rep", "inc_debt", "cat_inc_id", "user_inc_id", "wal_inc_id", "inc_name", "inc_date", "id", "inc_debt_to") SELECT "inc_rep", "inc_debt", "cat_inc_id", "user_inc_id", NULL, "inc_name", "inc_date", "id", "inc_debt_to" FROM "money_incomes__old";
DROP TABLE "money_incomes__old";
CREATE INDEX "money_incomes_f03f3b24" ON "money_incomes" ("cat_inc_id");
CREATE INDEX "money_incomes_31bd3004" ON "money_incomes" ("user_inc_id");
CREATE INDEX "money_incomes_9074e47f" ON "money_incomes" ("wal_inc_id");
--
-- Add field user_goal to goals
--
ALTER TABLE "money_goals" RENAME TO "money_goals__old";
CREATE TABLE "money_goals" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "goal_name" varchar(50) NOT NULL, "goal_amount" integer NOT NULL, "goal_deadline" date NOT NULL, "amount_now" integer NOT NULL, "user_goal_id" integer NOT NULL REFERENCES "money_users" ("id"));
INSERT INTO "money_goals" ("goal_amount", "goal_deadline", "amount_now", "goal_name", "user_goal_id", "id") SELECT "goal_amount", "goal_deadline", "amount_now", "goal_name", NULL, "id" FROM "money_goals__old";
DROP TABLE "money_goals__old";
CREATE INDEX "money_goals_81c4fa09" ON "money_goals" ("user_goal_id");
--
-- Add field user_exp to expenses
--
ALTER TABLE "money_expenses" RENAME TO "money_expenses__old";
CREATE TABLE "money_expenses" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "exp_name" varchar(50) NOT NULL, "exp_date" date NOT NULL, "exp_rep" integer NOT NULL, "exp_loan" bool NOT NULL, "exp_loan_to" varchar(50) NOT NULL, "cat_exp_id" integer NOT NULL REFERENCES "money_categories" ("id"), "user_exp_id" integer NOT NULL REFERENCES "money_users" ("id"));
INSERT INTO "money_expenses" ("exp_loan_to", "exp_loan", "exp_name", "exp_rep", "exp_date", "cat_exp_id", "user_exp_id", "id") SELECT "exp_loan_to", "exp_loan", "exp_name", "exp_rep", "exp_date", "cat_exp_id", NULL, "id" FROM "money_expenses__old";
DROP TABLE "money_expenses__old";
CREATE INDEX "money_expenses_e340c790" ON "money_expenses" ("cat_exp_id");
CREATE INDEX "money_expenses_a967c5b2" ON "money_expenses" ("user_exp_id");
--
-- Add field wal_exp to expenses
--
ALTER TABLE "money_expenses" RENAME TO "money_expenses__old";
CREATE TABLE "money_expenses" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "exp_name" varchar(50) NOT NULL, "exp_date" date NOT NULL, "exp_rep" integer NOT NULL, "exp_loan" bool NOT NULL, "exp_loan_to" varchar(50) NOT NULL, "cat_exp_id" integer NOT NULL REFERENCES "money_categories" ("id"), "user_exp_id" integer NOT NULL REFERENCES "money_users" ("id"), "wal_exp_id" integer NOT NULL REFERENCES "money_wallets" ("id"));
INSERT INTO "money_expenses" ("exp_loan_to", "exp_loan", "exp_name", "exp_rep", "wal_exp_id", "exp_date", "cat_exp_id", "user_exp_id", "id") SELECT "exp_loan_to", "exp_loan", "exp_name", "exp_rep", NULL, "exp_date", "cat_exp_id", "user_exp_id", "id" FROM "money_expenses__old";
DROP TABLE "money_expenses__old";
CREATE INDEX "money_expenses_e340c790" ON "money_expenses" ("cat_exp_id");
CREATE INDEX "money_expenses_a967c5b2" ON "money_expenses" ("user_exp_id");
CREATE INDEX "money_expenses_0198f2b0" ON "money_expenses" ("wal_exp_id");
--
-- Add field user_cat to categories
--
ALTER TABLE "money_categories" RENAME TO "money_categories__old";
CREATE TABLE "money_categories" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "cat_name" varchar(50) NOT NULL, "cat_for" integer NOT NULL, "user_cat_id" integer NOT NULL REFERENCES "money_users" ("id"));
INSERT INTO "money_categories" ("cat_for", "user_cat_id", "id", "cat_name") SELECT "cat_for", NULL, "id", "cat_name" FROM "money_categories__old";
DROP TABLE "money_categories__old";
CREATE INDEX "money_categories_ff69ac67" ON "money_categories" ("user_cat_id");
COMMIT;

BEGIN;
--
-- Add field balance to users
--
ALTER TABLE "money_users" RENAME TO "money_users__old";
CREATE TABLE "money_users" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "balance" integer NOT NULL, "user_name" varchar(50) NOT NULL, "e_mail" varchar(254) NOT NULL, "pass_word" varchar(100) NOT NULL, "currency" integer NOT NULL, "decimal" integer NOT NULL);
INSERT INTO "money_users" ("balance", "decimal", "e_mail", "currency", "pass_word", "user_name", "id") SELECT 0, "decimal", "e_mail", "currency", "pass_word", "user_name", "id" FROM "money_users__old";
DROP TABLE "money_users__old";
COMMIT;

BEGIN;
--
-- Add field wal_balance to wallets
--
ALTER TABLE "money_wallets" RENAME TO "money_wallets__old";
CREATE TABLE "money_wallets" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "wal_balance" integer NOT NULL, "wal_name" varchar(50) NOT NULL, "user_wal_id" integer NOT NULL REFERENCES "money_users" ("id"));
INSERT INTO "money_wallets" ("wal_balance", "wal_name", "id", "user_wal_id") SELECT 0, "wal_name", "id", "user_wal_id" FROM "money_wallets__old";
DROP TABLE "money_wallets__old";
CREATE INDEX "money_wallets_97d1e71a" ON "money_wallets" ("user_wal_id");
COMMIT;

BEGIN;
--
-- Alter field exp_loan_to on expenses
--
ALTER TABLE "money_expenses" RENAME TO "money_expenses__old";
CREATE TABLE "money_expenses" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "exp_loan_to" varchar(50) NOT NULL, "exp_name" varchar(50) NOT NULL, "exp_date" date NOT NULL, "exp_rep" integer NOT NULL, "exp_loan" bool NOT NULL, "cat_exp_id" integer NOT NULL REFERENCES "money_categories" ("id"), "user_exp_id" integer NOT NULL REFERENCES "money_users" ("id"), "wal_exp_id" integer NOT NULL REFERENCES "money_wallets" ("id"));
INSERT INTO "money_expenses" ("exp_loan_to", "exp_loan", "exp_name", "exp_rep", "wal_exp_id", "exp_date", "cat_exp_id", "user_exp_id", "id") SELECT "exp_loan_to", "exp_loan", "exp_name", "exp_rep", "wal_exp_id", "exp_date", "cat_exp_id", "user_exp_id", "id" FROM "money_expenses__old";
DROP TABLE "money_expenses__old";
CREATE INDEX "money_expenses_e340c790" ON "money_expenses" ("cat_exp_id");
CREATE INDEX "money_expenses_a967c5b2" ON "money_expenses" ("user_exp_id");
CREATE INDEX "money_expenses_0198f2b0" ON "money_expenses" ("wal_exp_id");
--
-- Alter field inc_debt_to on incomes
--
ALTER TABLE "money_incomes" RENAME TO "money_incomes__old";
CREATE TABLE "money_incomes" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "inc_name" varchar(50) NOT NULL, "inc_date" date NOT NULL, "inc_rep" integer NOT NULL, "inc_debt" bool NOT NULL, "cat_inc_id" integer NOT NULL REFERENCES "money_categories" ("id"), "user_inc_id" integer NOT NULL REFERENCES "money_users" ("id"), "wal_inc_id" integer NOT NULL REFERENCES "money_wallets" ("id"), "inc_debt_to" varchar(50) NOT NULL);
INSERT INTO "money_incomes" ("inc_rep", "inc_debt", "cat_inc_id", "user_inc_id", "wal_inc_id", "inc_name", "inc_date", "id", "inc_debt_to") SELECT "inc_rep", "inc_debt", "cat_inc_id", "user_inc_id", "wal_inc_id", "inc_name", "inc_date", "id", "inc_debt_to" FROM "money_incomes__old";
DROP TABLE "money_incomes__old";
CREATE INDEX "money_incomes_f03f3b24" ON "money_incomes" ("cat_inc_id");
CREATE INDEX "money_incomes_31bd3004" ON "money_incomes" ("user_inc_id");
CREATE INDEX "money_incomes_9074e47f" ON "money_incomes" ("wal_inc_id");
COMMIT;

BEGIN;
--
-- Alter field exp_loan_to on expenses
--
ALTER TABLE "money_expenses" RENAME TO "money_expenses__old";
CREATE TABLE "money_expenses" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "exp_loan_to" varchar(50) NULL, "exp_name" varchar(50) NOT NULL, "exp_date" date NOT NULL, "exp_rep" integer NOT NULL, "exp_loan" bool NOT NULL, "cat_exp_id" integer NOT NULL REFERENCES "money_categories" ("id"), "user_exp_id" integer NOT NULL REFERENCES "money_users" ("id"), "wal_exp_id" integer NOT NULL REFERENCES "money_wallets" ("id"));
INSERT INTO "money_expenses" ("exp_loan_to", "exp_loan", "exp_name", "exp_rep", "wal_exp_id", "exp_date", "cat_exp_id", "user_exp_id", "id") SELECT "exp_loan_to", "exp_loan", "exp_name", "exp_rep", "wal_exp_id", "exp_date", "cat_exp_id", "user_exp_id", "id" FROM "money_expenses__old";
DROP TABLE "money_expenses__old";
CREATE INDEX "money_expenses_e340c790" ON "money_expenses" ("cat_exp_id");
CREATE INDEX "money_expenses_a967c5b2" ON "money_expenses" ("user_exp_id");
CREATE INDEX "money_expenses_0198f2b0" ON "money_expenses" ("wal_exp_id");
--
-- Alter field inc_debt_to on incomes
--
ALTER TABLE "money_incomes" RENAME TO "money_incomes__old";
CREATE TABLE "money_incomes" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "inc_name" varchar(50) NOT NULL, "inc_date" date NOT NULL, "inc_rep" integer NOT NULL, "inc_debt" bool NOT NULL, "cat_inc_id" integer NOT NULL REFERENCES "money_categories" ("id"), "user_inc_id" integer NOT NULL REFERENCES "money_users" ("id"), "wal_inc_id" integer NOT NULL REFERENCES "money_wallets" ("id"), "inc_debt_to" varchar(50) NULL);
INSERT INTO "money_incomes" ("inc_rep", "inc_debt", "cat_inc_id", "user_inc_id", "wal_inc_id", "inc_name", "inc_date", "id", "inc_debt_to") SELECT "inc_rep", "inc_debt", "cat_inc_id", "user_inc_id", "wal_inc_id", "inc_name", "inc_date", "id", "inc_debt_to" FROM "money_incomes__old";
DROP TABLE "money_incomes__old";
CREATE INDEX "money_incomes_f03f3b24" ON "money_incomes" ("cat_inc_id");
CREATE INDEX "money_incomes_31bd3004" ON "money_incomes" ("user_inc_id");
CREATE INDEX "money_incomes_9074e47f" ON "money_incomes" ("wal_inc_id");
COMMIT;

BEGIN;
--
-- Add field exp_amount to expenses
--
ALTER TABLE "money_expenses" RENAME TO "money_expenses__old";
CREATE TABLE "money_expenses" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "exp_amount" integer NOT NULL, "exp_name" varchar(50) NOT NULL, "exp_date" date NOT NULL, "exp_rep" integer NOT NULL, "exp_loan" bool NOT NULL, "exp_loan_to" varchar(50) NULL, "cat_exp_id" integer NOT NULL REFERENCES "money_categories" ("id"), "user_exp_id" integer NOT NULL REFERENCES "money_users" ("id"), "wal_exp_id" integer NOT NULL REFERENCES "money_wallets" ("id"));
INSERT INTO "money_expenses" ("exp_loan_to", "exp_loan", "exp_name", "exp_rep", "wal_exp_id", "exp_date", "cat_exp_id", "user_exp_id", "id", "exp_amount") SELECT "exp_loan_to", "exp_loan", "exp_name", "exp_rep", "wal_exp_id", "exp_date", "cat_exp_id", "user_exp_id", "id", 1 FROM "money_expenses__old";
DROP TABLE "money_expenses__old";
CREATE INDEX "money_expenses_e340c790" ON "money_expenses" ("cat_exp_id");
CREATE INDEX "money_expenses_a967c5b2" ON "money_expenses" ("user_exp_id");
CREATE INDEX "money_expenses_0198f2b0" ON "money_expenses" ("wal_exp_id");
--
-- Add field inc_amount to incomes
--
ALTER TABLE "money_incomes" RENAME TO "money_incomes__old";
CREATE TABLE "money_incomes" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "inc_name" varchar(50) NOT NULL, "inc_date" date NOT NULL, "inc_rep" integer NOT NULL, "inc_debt" bool NOT NULL, "inc_debt_to" varchar(50) NULL, "cat_inc_id" integer NOT NULL REFERENCES "money_categories" ("id"), "user_inc_id" integer NOT NULL REFERENCES "money_users" ("id"), "wal_inc_id" integer NOT NULL REFERENCES "money_wallets" ("id"), "inc_amount" integer NOT NULL);
INSERT INTO "money_incomes" ("inc_rep", "inc_amount", "inc_debt", "cat_inc_id", "user_inc_id", "wal_inc_id", "inc_name", "inc_date", "id", "inc_debt_to") SELECT "inc_rep", 1, "inc_debt", "cat_inc_id", "user_inc_id", "wal_inc_id", "inc_name", "inc_date", "id", "inc_debt_to" FROM "money_incomes__old";
DROP TABLE "money_incomes__old";
CREATE INDEX "money_incomes_f03f3b24" ON "money_incomes" ("cat_inc_id");
CREATE INDEX "money_incomes_31bd3004" ON "money_incomes" ("user_inc_id");
CREATE INDEX "money_incomes_9074e47f" ON "money_incomes" ("wal_inc_id");
COMMIT;

BEGIN;
--
-- Alter field exp_amount on expenses
--
ALTER TABLE "money_expenses" RENAME TO "money_expenses__old";
CREATE TABLE "money_expenses" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "exp_amount" real NOT NULL, "exp_name" varchar(50) NOT NULL, "exp_date" date NOT NULL, "exp_rep" integer NOT NULL, "exp_loan" bool NOT NULL, "exp_loan_to" varchar(50) NULL, "cat_exp_id" integer NOT NULL REFERENCES "money_categories" ("id"), "user_exp_id" integer NOT NULL REFERENCES "money_users" ("id"), "wal_exp_id" integer NOT NULL REFERENCES "money_wallets" ("id"));
INSERT INTO "money_expenses" ("exp_loan_to", "exp_loan", "exp_name", "exp_rep", "wal_exp_id", "exp_date", "cat_exp_id", "user_exp_id", "id", "exp_amount") SELECT "exp_loan_to", "exp_loan", "exp_name", "exp_rep", "wal_exp_id", "exp_date", "cat_exp_id", "user_exp_id", "id", "exp_amount" FROM "money_expenses__old";
DROP TABLE "money_expenses__old";
CREATE INDEX "money_expenses_e340c790" ON "money_expenses" ("cat_exp_id");
CREATE INDEX "money_expenses_a967c5b2" ON "money_expenses" ("user_exp_id");
CREATE INDEX "money_expenses_0198f2b0" ON "money_expenses" ("wal_exp_id");
--
-- Alter field inc_amount on incomes
--
ALTER TABLE "money_incomes" RENAME TO "money_incomes__old";
CREATE TABLE "money_incomes" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "inc_name" varchar(50) NOT NULL, "inc_date" date NOT NULL, "inc_rep" integer NOT NULL, "inc_debt" bool NOT NULL, "inc_debt_to" varchar(50) NULL, "cat_inc_id" integer NOT NULL REFERENCES "money_categories" ("id"), "user_inc_id" integer NOT NULL REFERENCES "money_users" ("id"), "wal_inc_id" integer NOT NULL REFERENCES "money_wallets" ("id"), "inc_amount" real NOT NULL);
INSERT INTO "money_incomes" ("inc_rep", "inc_amount", "inc_debt", "cat_inc_id", "user_inc_id", "wal_inc_id", "inc_name", "inc_date", "id", "inc_debt_to") SELECT "inc_rep", "inc_amount", "inc_debt", "cat_inc_id", "user_inc_id", "wal_inc_id", "inc_name", "inc_date", "id", "inc_debt_to" FROM "money_incomes__old";
DROP TABLE "money_incomes__old";
CREATE INDEX "money_incomes_f03f3b24" ON "money_incomes" ("cat_inc_id");
CREATE INDEX "money_incomes_31bd3004" ON "money_incomes" ("user_inc_id");
CREATE INDEX "money_incomes_9074e47f" ON "money_incomes" ("wal_inc_id");
COMMIT;

BEGIN;
--
-- Alter field currency on users
--
ALTER TABLE "money_users" RENAME TO "money_users__old";
CREATE TABLE "money_users" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "currency" varchar(20) NOT NULL, "user_name" varchar(50) NOT NULL, "e_mail" varchar(254) NOT NULL, "pass_word" varchar(100) NOT NULL, "decimal" integer NOT NULL, "balance" integer NOT NULL);
INSERT INTO "money_users" ("balance", "decimal", "e_mail", "currency", "pass_word", "user_name", "id") SELECT "balance", "decimal", "e_mail", "currency", "pass_word", "user_name", "id" FROM "money_users__old";
DROP TABLE "money_users__old";
COMMIT;

BEGIN;
--
-- Remove field e_mail from users
--
ALTER TABLE "money_users" RENAME TO "money_users__old";
CREATE TABLE "money_users" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_name" varchar(50) NOT NULL, "pass_word" varchar(100) NOT NULL, "currency" varchar(20) NOT NULL, "decimal" integer NOT NULL, "balance" integer NOT NULL);
INSERT INTO "money_users" ("balance", "decimal", "currency", "pass_word", "user_name", "id") SELECT "balance", "decimal", "currency", "pass_word", "user_name", "id" FROM "money_users__old";
DROP TABLE "money_users__old";
--
-- Remove field pass_word from users
--
ALTER TABLE "money_users" RENAME TO "money_users__old";
CREATE TABLE "money_users" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_name" varchar(50) NOT NULL, "currency" varchar(20) NOT NULL, "decimal" integer NOT NULL, "balance" integer NOT NULL);
INSERT INTO "money_users" ("balance", "decimal", "currency", "user_name", "id") SELECT "balance", "decimal", "currency", "user_name", "id" FROM "money_users__old";
DROP TABLE "money_users__old";
COMMIT;
