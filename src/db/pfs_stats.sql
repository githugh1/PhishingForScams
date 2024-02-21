DROP DATABASE IF EXISTS `pfs_stats`;
CREATE DATABASE `pfs_stats`;
USE `pfs_stats`;

# Common database for all services

CREATE TABLE main (
  id TEXT NOT NULL,
  item_source TEXT DEFAULT NULL,
  time_sent datetime DEFAULT NULL,
  item_key TEXT DEFAULT NULL,
  item_val LONGTEXT NOT NULL
);

# Example input format

INSERT INTO main (id, item_source, time_sent, item_key, item_val)
VALUES("<acf26712000020a1@comsoft.co.in>", "scanner", now(), "result", "SCAM");

INSERT INTO main (id, item_source, time_sent, item_key, item_val)
VALUES("<xyz123456789@fakeemail.com>", "scanner", '2024-02-18 12:34:56', "outcome", "SCAM");

INSERT INTO main (id, item_source, time_sent, item_key, item_val)
VALUES("<789abcde0123456@scamalert.net>", "scanner", '2024-02-18 08:15:30', "status", "SCAM");

INSERT INTO main (id, item_source, time_sent, item_key, item_val)
VALUES("<qwerty123@phishingtrap.com>", "scanner", '2024-02-18 15:45:00', "flag", "SAFE");

INSERT INTO main (id, item_source, time_sent, item_key, item_val)
VALUES("<def456789012345@spamscanner.io>", "scanner", '2024-02-18 14:25:00', "scan_result", "SCAM");

INSERT INTO main (id, item_source, time_sent, item_key, item_val)
VALUES("<4567890123abcde@fraudalert.com>", "scanner", '2024-02-18 09:30:45', "alert_status", "SAFE");

INSERT INTO main (id, item_source, time_sent, item_key, item_val)
VALUES("<678901234defg@securityservice.net>", "scanner", '2024-02-18 11:11:11', "warning_message", "SCAM");

/*INSERT INTO main (id, item_source, time_sent, item_key, item_val)
VALUES
("<acf26712000020a1@comsoft.co.in>",
"parser", 
now(), 
"full_eml", 
'{
    "headers": {
        "X-Gm-Message-State": [
            "AOJu0YzVHwzkPbUS3REZpykF2jkMjVTlYgoIETGboT68qtn2rT4lzQmA\tlg2cNlQH4otog6lLn8ZojmtQQMmaStClpRFSiDOZQgT66rIV0g=="
        ],
        "X-Google-Smtp-Source": [
            "AGHT+IEK1IT2qY7A0IYYApIWB2Kk/ZOLi5DUQbaaadF4Cz6lEcwJzZadW7hMaZdOP0ZnDuF8UtbuutUId6ii"
        ],
        "X-Received": [
            "by 2002:a05:6e02:1565:b0:359:5b5c:9ce4 with SMTP id k5-20020a056e02156500b003595b5c9ce4mr1219131ilu.19.1699421955123; Tue, 07 Nov 2023 21:39:15 -0800 (PST)",
            "by 2002:a05:6e02:1b8d:b0:351:4b68:ec3a with SMTP id h13-20020a056e021b8d00b003514b68ec3amr1230718ili.9.1699421954854; Tue, 07 Nov 2023 21:39:14 -0800 (PST)"
        ],
        "ARC-Authentication-Results": [
            "i=1; mx.google.com; dkim=pass header.i=@comsoft-com-sg.20230601.gappssmtp.com header.s=20230601 header.b=\"Tj/y/JWh\"; spf=pass (google.com: domain of amols@comsoft.co.in designates 209.85.220.101 as permitted sender) smtp.mailfrom=amols@comsoft.co.in"
        ],
        "Received-SPF": [
            "pass (google.com: domain of amols@comsoft.co.in designates 209.85.220.101 as permitted sender) client-ip=209.85.220.101;"
        ],
        "X-Tm-Imss-Message-Id": [
            "<acf26712000020a1@comsoft.co.in>"
        ],
        "Received": [
            "by 2002:a05:7022:ff46:b0:6e:5bd9:4d3c with SMTP id vp6csp748810dlb; Tue, 7 Nov 2023 21:39:15 -0800 (PST)",
            "from mail-sor-f101.google.com (mail-sor-f101.google.com. [209.85.220.101]) by mx.google.com with SMTPS id w5-20020a92d2c5000000b00359311f482csor2987365ilg.7.2023.11.07.21.39.14 for <samih.hijwel@gmail.com> (Google Transport Security); Tue, 07 Nov 2023 21:39:15 -0800 (PST)",
            "from admin.comsoft.co.in ([114.143.189.38]) by smtp-relay.gmail.com with ESMTP id z9-20020a92d189000000b00351058205f7sm507228ilz.65.2023.11.07.21.39.10; Tue, 07 Nov 2023 21:39:14 -0800 (PST)",            "from mail.comsoft.co.in ([192.168.1.80]) by comsoft.co.in ([192.168.1.98]) with ESMTP (TREND IMSS SMTP Service 7.1) id acf26712000020a1 ; Wed, 8 Nov 2023 05:32:20 +0530",
            "from User (unknown [80.94.92.103])\t(Authenticated sender: amols@comsoft.co.in)\tby mail.comsoft.co.in (Postfix) with ESMTPA id EC2B2141664;\tWed, 8 Nov 2023 05:32:07 +0530 (IST)"
        ],
        "X-Priority": [
            "3"
        ],
        "ARC-Seal": [
            "i=1; a=rsa-sha256; t=1699421955; cv=none; d=google.com; s=arc-20160816; b=TFN557qrMWygKPBGPvZz9wrg+SY1UYFTWaY+v6g+jogOL6+C+ksXfJKogXxRPYmZ3y cfI/XjSpSnvXpP5fA2Je0Qyb6LuaPDWNTLJJIsr4ezJMIkgCvuAL/sChlJzY5OxTP8yF Xyxqu5FT8Zv28p0VCgETTEDMw0KgvFgGPXwuu1ZswXdueMObV92aBKU5qsOuH10g6Ftt 2tM/5Tiobw8A1TK3Olf4z/24kHWReeyCjQ28qisE+LDmwjcO0Xs6cdeiUk6/uFJ+MPvk 1/4jDbNlUCnLNSMMODG4oXG4AuQUF1YrY8Flifj5ic2AyV4OMg2ty2hx+I7mUs10YmD9 0qcw=="
        ],
        "X-Mailer": [
            "Microsoft Outlook Express 6.00.2600.0000"
        ],
        "X-Msmail-Priority": [
            "Normal"
        ],
        "ARC-Message-Signature": [
            "i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816; h=content-transfer-encoding:mime-version:date:subject:from:reply-to :message-id:dkim-signature; bh=6x9E0v7D2j0gJ/x1mko2tz3sfW55OfpP+m4qFPha2Uk=; fh=47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=; b=drCayxAXYnDDZs75j9FASCn8sDckI+QtrLih6/QxrDqBrsNsWwO10iO/NW3OrslOAg ZVFtJk318kklNJ8zenCKhW1PM8JkjPY4N2XYjvVVTwpUVJJQVSrA5SxCgvp9rfjvaZin FOscSS0l4qwCUFKiEUhOQRNkTapXiDk+KlZSxvzHYpEuTUYcLE2aCX7q31HFAi4U4Lve vzC3Tc/OikPL87wX1MmcSz2MHkkdMa4JCmOXrOp0vobjrvaKX2HqzqBYOz9tbNShA2xa V44gOUTgrdBfNcXipxx0e98W4I5MgCUOYA4JcVnDx1p9oNkvzh41KwTGePptdPxkST5e 9MkQ=="
        ],
        "X-Google-DKIM-Signature": [
            "v=1; a=rsa-sha256; c=relaxed/relaxed; d=1e100.net; s=20230601; t=1699421954; x=1700026754; h=content-transfer-encoding:mime-version:date:subject:from:reply-to :message-id:x-gm-message-state:from:to:cc:subject:date:message-id :reply-to; bh=6x9E0v7D2j0gJ/x1mko2tz3sfW55OfpP+m4qFPha2Uk=; b=v6T2ZZ+EdS3P3uR/PFZmeYxPMfRBK1F8fCFdE5FAb2ViMeA4hY67jxzC2GV8XABdZX WcdFDD0YMM8Dh1XR3mNW7rSvEO18U6kcdZw/Om0ywfuZ/r5vNheFRDUVAm+dMxs9fd/D DSFruAj+QDtPXMP/S/pG/+ZG8MGggmGWq36yB/0dO8bDkJy/RQOww6ESczXWVflHl92U yoMKL1g2MXnb/02PpL9BU4LtFqUUDorsksl+sGkxGCjS93pLGEvN9YkmyEolexPWls80 909Ol1vtCCyarWs58PScgtS0vKLQaiN7niuePUOYeB3ps12+j9wwI8WzXAqLEHoJMsaZ rDrA=="
        ],
        "X-Mimeole": [
            "Produced By Microsoft MimeOLE V6.00.2600.0000"
        ],
        "Mime-Version": "1.0",
        "X-Relaying-Domain": [
            "comsoft.co.in"
        ],
        "Delivered-To": {
            "name": null,
            "email": "samih.hijwel@gmail.com"
        },
        "Authentication-Results": [
            "mx.google.com; dkim=pass header.i=@comsoft-com-sg.20230601.gappssmtp.com header.s=20230601 header.b=\"Tj/y/JWh\"; spf=pass (google.com: domain of amols@comsoft.co.in designates 209.85.220.101 
as permitted sender) smtp.mailfrom=amols@comsoft.co.in"
        ],
        "DKIM-Signature": [
            "v=1; a=rsa-sha256; c=relaxed/relaxed; d=comsoft-com-sg.20230601.gappssmtp.com; s=20230601; t=1699421954; x=1700026754; dara=google.com; h=content-transfer-encoding:mime-version:date:subject:from:reply-to :message-id:from:to:cc:subject:date:message-id:reply-to; bh=6x9E0v7D2j0gJ/x1mko2tz3sfW55OfpP+m4qFPha2Uk=; b=Tj/y/JWhsMZ7oZOTlYJ7Z7b2U0RYFON67K5GxgYeQXG6J8KQOshXGVKxcGiC0Pl47x aX8zdabvAS3pQaBMtJMFvKmYZ/izYHpcs0O4KNStGfdAAm3/LI2TgtWDo152HLmGxCOc MiTnoXzmaoqKl8rDmyH5qf/AH8WMtx2M22ZTqMPq/N2Mg2xjSsEzfKFfwtXGQ8QPh5qu u7jn6spvVNeiBCqxo0lgPiCnzMfnGr74AWfw7R3BYF63jfDCGKy6CTIfeIsYJtbknUXV MXFgQEdkeAgER9R9DAV3hhRxIcTc3zsSa1xYguoPdZgObJa1Mu6LQ0FSw+x7l8Y1q+TQ ywbw=="
        ],
        "Reply-To": [
            {
                "name": null,
                "email": "lyneahmd@gmail.com"
            }
        ]
    },
    "text": "I hope this letter finds you in good health and high spirits. My name is  Mrs. Lynn Berrycloth, and I write to you with the utmost respect and  sincerity. Please allow me to apologize for any 
inconvenience caused by  reaching out to you through this electronic medium. However, I find  myself compelled to seek your assistance in fulfilling a charitable  project, which holds great importance to me in light of my  circumstances. I want to donate my inheritance ($20Million US Dollars)  that my late husband left for me before he died in 2013 in a Spanish  train crash that took him away from me.\r\n\r\nIt is with a heavy heart that I reveal my ongoing battle with cancer, a  diagnosis I am battling with for six years. Despite the challenges and  uncertainty that this illness has brought into my life, I 
have chosen to remain optimistic and resilient. As I face the inevitable, I am  determined to make a positive impact and leave a lasting legacy of  kindness and compassion.\r\n\r\nI want you to use 30% of 
the fund to build orphanage homes in your  country while 20% goes to cancer research programs and then donate 25%  to institutions housing elderly couples who cannot give birth and  homeless children in their lifetime just like my late husband and I  could not bear children. The remaining 25% goes to you as the person who agrees to carry out my last wish and I will give you more details only  if you are willing and ready to handle this project. I humbly request  your prompt response, expressing your willingness to assist me in  fulfilling my last wish.\r\n\r\nThank you for your attention, and I eagerly await your favorable reply.\r\n\r\nWarm regards,\r\n\r\nMrs. Lynn Berrycloth",
    "html": null,
    "message-id": "<acf26712000020a1@comsoft.co.in>",
    "from": {
        "name": "Lynn Berrycloth",
        "email": "amols@comsoft.co.in"
    },
    "return-path": {
        "name": null,
        "email": "amols@comsoft.co.in"
    },
    "subject": "Donation.",
    "date": "Tue, 7 Nov 2023 16:02:19 -0800",
    "timestamp": 1699401739
}');*/