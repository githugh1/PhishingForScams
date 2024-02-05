# Welcome to the MailService!

## Structure

### Getmail

Getmail makes use of the getmail6 package to pull emails from a target server protocol, including IMAP, POP3 and SDPS. Retriever types can be found [here](https://getmail6.org/configuration.html). Getmail contains a `getmailrc` file, which can be configured to pull from any server outlined in the config (e.g. imap.gmail.com). The getmail dir will also contain a log of any previously pulled emails, so duplicates are not created. This can be adjusted by setting `read_all` to true in the config.

When setting up the config, it is ideal to use an app password when possible, to reduce the chance of unnecessary errors occuring when using certain platforms (e.g. gmail). The inboxes tag can be adjusted to include/exclude any target inboxes. Leave blank to select them all.

### Mail

This directory is used to store the emails. A docker volume is created in the `docker-compose.yml` for this very purpose.