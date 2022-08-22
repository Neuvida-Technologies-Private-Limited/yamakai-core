"""
Create user related queries for analytics.
"""
user_queries = {
    # "Total Signups": "select count(*) as 'Total Signups' from access_user",
    # "Total Signups SSO": "select count(*) as 'Total Signups SSO' \
    #                     from access_user where is_sso=1",
    # "Total Signups Phone": "select count(*) as 'Total Signups \
    #                         PHONE' from access_user where phone \
    #                         IS NOT NULL",
    # "Total Signups Email": "select count(*) as 'Total Signups EMAIL' from access_user \
    #                         where email IS NOT NULL and is_sso = 0",
    # "Total Signups SSO (%)": "select (select count(*) from access_user \
    #                         where is_sso=1) \
    #                         / (select count(*) from access_user) * 100 \
    #                         as 'Total Signups SSO (%)'",
    # "Total Signups Phone (%)": "select (select count(*) from access_user where phone \
    #                         IS NOT NULL) \
    #                         / (select count(*) from access_user) * 100 as \
    #                         'Total Signups PHONE (%)'",
    # "Total Signups Email (%)": "select (select count(*) from access_user where email IS NOT \
    #                             NULL and is_sso=0) / (select count(*) from access_user) * \
    #                             100 as 'Total Signups EMAIL (%)' \
    #                             NULL and is_sso=0) (select count(*) from access_user) * \
    #                             100 as 'Total Signups EMAIL (%)'",
    # "Monthly Signups": "SELECT LEFT(created_at, 7) AS Month, \
    #                          COUNT(id) AS 'Monthly signups' \
    #                          FROM access_user \
    #                         GROUP BY LEFT(created_at, 7)",
    # "Daily Signups":"SELECT DATE(created_at) AS DAY, \
    #                       COUNT(id) AS 'Daily signups' \
    #                       FROM access_user \
    #                       GROUP BY DATE(created_at)\
    #                       ORDER BY DAY DESC\
    #                        LIMIT 30;",
    # "Weekly active users":"SELECT WEEK(created_at) AS WEEK, \
    #                        COUNT(DISTINCT created_by_id) AS WAU \
    #                        FROM utils_gpt3outputs \
    #                        GROUP BY WEEK(created_at) \
    #                        ORDER BY WEEK DESC \
    #                        LIMIT 4;",
    # "Monthly active users":"SELECT MONTH(created_at) AS MONTH, \
    #                        COUNT(DISTINCT created_by_id) AS MAU \
    #                        FROM utils_gpt3outputs \
    #                        GROUP BY MONTH(created_at) \
    #                        ORDER BY MONTH DESC;",                       
    # "I/O Template":"SELECT a.user_id_id AS user_id, \
    #                 a.template_name AS template,\
    #                 a.input,\
    #                 b.output \
    #                 FROM utils_userinputs AS a \
    #                 JOIN utils_gpt3outputs AS b ON a.id  = b.user_input_id_id \
    #                 WHERE a.template_name = 'SUBJECT_LINE' \
    #                 ORDER BY a.user_id_id",
    # "Total signups":"SELECT COUNT(DISTINCT id) AS 'Total signups' \
    #                  FROM access_user;",
    "Power users":  "SELECT b.id,\
	                        b.repeat_days,\
                            au.phone,\
                            au.email, \
                            au.first_name,\
                            au.last_name \
                     FROM (SELECT id, COUNT(*) repeat_days \
	                       FROM (SELECT DATE(created_at) AS date, \
                                        created_by_id AS id \
                                 FROM utils_gpt3outputs \
                                 GROUP BY DATE(created_at),created_by_id \
                                 ORDER BY date DESC) a \
                           GROUP BY id \
                           HAVING COUNT(*) > 1 \
                           ORDER BY id) b \
                     JOIN access_user AS au ON b.id = au.id"
}
# repeat_users = {
#     "Total template usage": "SELECT count(template_name) AS total_template_name, \
#                             template_name FROM utils_userinputs GROUP BY \
#                             template_name ORDER BY total_template_name",
#     "Users Email": "select access_user.email as email, \
#                     first_name, last_name, date_format(utils_userinputs.created_at, \
#                    '%Y-%m-%d') as ran_at, template_name \
#                     from access_user cross join \
#                     utils_userinputs on access_user.id = utils_userinputs.user_id_id \
#                     where email NOT IN ('vishalsingh1080@gmail.com', \
#                     'vishalkonline@gmail.com','vishal25797.work@gmail.com', \
#                     'vishal@yamak.ai', 'vipuldhiman24@gmail.com', \
#                     'srashti.ss03@gmail.com', 'shivammaddhesia0419@gmail.com', \
#                     'saurav.suman.319@gmail.com', 'rishabhb932@gmail.com', 'rasick@gmail.com', \
#                     'preethiknot1998@gmail.com', 'preethi@yamak.ai', 'bhardwaj.1@iitj.ac.in', \
#                     'admin@yamak.ai', 'abhinav.rai.1996@gmail.com', \
#                     'me.2019.bktaksande@bitwardha.ac.in', \
#                     'srashti.1531163@kiet.edu', 'srashti1163@gmail.com') \
#                     ORDER BY email, ran_at",
#     "Users Phone": "select access_user.phone as phone, access_user.email as email, \
#                     first_name, last_name, date_format(utils_userinputs.created_at, \
#                     '%Y-%m-%d') as ran_at, template_name from access_user cross join \
#                     utils_userinputs on access_user.id = utils_userinputs.user_id_id \
#                     where phone NOT IN ('8920564682', '9884209831', '9359489538', \
#                     '7899422725', '7042857001', '') ORDER BY phone, ran_at"
# }
