#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_job_with_filter(dbconn, performer, discriminator, filter=""):
    if filter is None:
        filter = ""
    query = "SELECT "
    if dbconn.engine == 'mssql':
        query = query + " TOP 10 "
    query = query + "a.id FROM sungero_wf_assignment a " \
            + "WHERE a.performer = {0} ".format(performer) \
            + "AND a.status = 'InProcess' " \
            + "AND a.discriminator = '{0}' ".format(discriminator) \
            + "AND a.subject like '%{0}%' ".format(filter) \
            + "ORDER BY created desc "
    if dbconn.engine == 'psql':
        query = query \
                + "LIMIT 10"

    with dbconn.connection() as connection:
        cur = connection.cursor()
        cur.execute(query)
        result = cur.fetchall()
        return result



def get_all_jobs(dbconn, performer, discriminator, skip):
    query = "SELECT "

    query = query + "a.id FROM sungero_wf_assignment a " \
            + "WHERE a.performer = {0} ".format(performer) \
            + "AND a.status = 'InProcess' " \
            + "AND a.discriminator = '{0}' ".format(discriminator) \
            + "ORDER BY created desc "
    if dbconn.engine == 'psql':
        query = query + "OFFSET {0}".format(skip)
    if dbconn.engine == 'mssql':
        query = query + "OFFSET ({0}) ROWS".format(skip)

    with dbconn.connection() as connection:
        cur = connection.cursor()
        cur.execute(query)
        result = cur.fetchall()
        return result

    
    
def get_task_with_filter(dbconn, author, discriminator, filter=""):
    if filter is None:
        filter = ""
    query = "SELECT "
    if dbconn.engine == 'mssql':
        query = query + " TOP 10 "
    query = query + "t.id FROM sungero_wf_task t " \
            + "WHERE t.author = {0} ".format(author) \
            + "AND t.status = 'InProcess' " \
            + "AND t.discriminator = '{0}' ".format(discriminator) \
            + "AND t.subject like '%{0}%' ".format(filter) \
            + "ORDER BY created desc "
    if dbconn.engine == 'psql':
        query = query \
                + "LIMIT 10"

    with dbconn.connection() as connection:
        cur = connection.cursor()
        cur.execute(query)
        result = cur.fetchall()
        return result
