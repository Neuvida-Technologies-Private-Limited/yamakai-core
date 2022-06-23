user_queries = {
    "Total Signups": "select count(*) as 'Total Signups' from access_user",
    "Total Signups SSO": "select count(*) as 'Total Signups SSO' \
                        from access_user where is_sso=1",
    "Total Signups Phone": "select count(*) as 'Total Signups PHONE' from access_user where phone IS NOT NULL",
    "Total Signups Email": "select count(*) as 'Total Signups EMAIL' from access_user where email IS NOT NULL and is_sso = 0",
    "Total Signups SSO (%)": "select (select count(*) from access_user where is_sso=1) \
                            / (select count(*) from access_user) * 100 as 'Total Signups SSO (%)'",
    "Total Signups Phone (%)": "select (select count(*) from access_user where phone IS NOT NULL) \
                        / (select count(*) from access_user) * 100 as 'Total Signups PHONE (%)'",
    "Total Signups Email (%)": "select (select count(*) from access_user where email IS NOT NULL and is_sso=0) \
                        / (select count(*) from access_user) * 100 as 'Total Signups EMAIL (%)'",
}
repeat_users = {
    "Repeat Users": "select access_user.phone as phone, access_user.email as email, \
                    first_name, last_name, date_format(utils_userinputs.created_at, '%Y-%m-%d') as ran_at, template_name \
                    from access_user cross join utils_userinputs on access_user.id = utils_userinputs.user_id_id \
                    ORDER BY email, phone"
    # \
    #                 where email NOT IN ('admin@gmail.com', 'vipuldhiman24@gmail.com', 'preethi@yamak.ai', 'shivam@yamak.ai', \
    #                 'admin@yamak.ai', 'preethiknot1998@gmail.com', 'vishalsingh1080@gmail.com', '123@gmail.com', \
    #                 'shivammaddhesia0419@gmail.com', 'vishal@yamak.ai', 'vishal25797.work@gmail.com', 'bhardwaj.1@iitj.ac.in', \
    #                 'future.srashti@gmail.com', 'uditkg@gmail.com', 'aaa@gmail.com', 'abc@gmail.com', 'aaaa@aaaa.com', \
    #                 'Preethiknot1998@gmail.co', 'rishabhb932@gmail.com', 'saurav.suman.319@gmail.com')"
}

