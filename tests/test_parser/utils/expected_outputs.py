EXPECTED_EML_1 = {
    'headers': 
        {'ARC-Seal': ['i=1; a=rsa-sha256; t=1701792540; cv=none; d=google.com; s=arc-20160816; b=UTh9OKbORMKwpLkG0x5LSYuQS2D3KPigX2ljetNWc5Ah0+feScauQf2l/uq/8TDPZT C7uQVDc8RXWDc398u4eDlHEK79NPy79fFwG4n34+JNPdxFVwZ2XXjBmq5g4jTbnjEqQI p28hEY68LSbk70l0RowN8LcMqTRBz4m7IIoztyWa6oexW63BPDz/LA28mZ64PckeQRoA 3MZHFLkS8fpdhWFkUQJFZ2WAOUvzuWxV5QuBF9gCE1wBoGWsbWyfnYhNfxlI/Vsfrpi4 rCWjxK9a8wwaOHtDenZki4b6HjG/J+lFBqgg9z/orKa21ChlQRNlIIphVm3jWJsRYyXT 7QLQ=='], 
         'ARC-Message-Signature': ['i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816; h=reply-to:date:from:to:subject:content-description :content-transfer-encoding:mime-version:message-id; bh=10P/O8XemFyCWfDmMcvPR0tRW8YApiVPw2fmXzcZ7HY=; fh=wnDD4oYUTIkRagM/TZ2HlBrNiOeZgfXs5zv+5cBmKR8=; b=Se4SzdtAXVU1kZXonkFsGMBbBdz2eGIbbkfZVj+t1n818MHAk3P7pUDa9Py2fkq6LK X2+mT2VVqlzkiiE93WtLDhPk6WD/cvy0aY5XbWSYI3x+cU3XwH3+PlOHa2pouROcdvIS fWSrl/w+l+WS98QS6ot38O09+nsc3xhQfrubldPdGFT4QpSyOHd3ReognbmhoEMjitPC 3tfoRt7qaoVv05NdkOi3bOI0RhbtH0jZ18YZ9vOpqCzBNQ0O+fIJjA3OobR9nYZieSRO 0wBpZO6R6ZN2L0ws6ycp/2/AG9CwU7QyB9OytYRY38fWd2umDeZ7T09QsbBgqit5ZQan 60MQ=='], 
         'Mime-Version': '1.0', 'Authentication-Results': ['mx.google.com; spf=pass (google.com: domain of asley.cristales@sifei.com.mx designates 35.162.214.19 as permitted sender) smtp.mailfrom=asley.cristales@sifei.com.mx'], 
         'Received': ['by 2002:a05:7022:221f:b0:6e:5bd9:4d3c with SMTP id bu31csp2115533dlb; Tue, 5 Dec 2023 08:09:00 -0800 (PST)', 'from siweaws.sifei.com.mx (mx20.sifei.com.mx. [35.162.214.19]) by mx.google.com with ESMTP id h1-20020a635741000000b005a9c40151b3si6343197pgm.804.2023.12.05.08.09.00; Tue, 05 Dec 2023 08:09:00 -0800 (PST)', 'from mail.sifei.com.mx (ip-10-2-0-6.us-west-2.compute.internal [10.2.0.6])\tby siweaws.sifei.com.mx (Postfix) with ESMTP id 5DBED423521;\tTue, 5 Dec 2023 10:08:21 -0600 (CST)', 'from [91.92.243.107] (unknown [91.92.243.107])\tby mail.sifei.com.mx (Postfix) with ESMTPSA id 2D89636F8685;\tTue, 5 Dec 2023 10:06:36 -0600 (CST)'], 'Reply-To': [{'name': None, 'email': 'jonahaskel63@gmail.com'}], 'ARC-Authentication-Results': ['i=1; mx.google.com; spf=pass (google.com: domain of asley.cristales@sifei.com.mx designates 35.162.214.19 as permitted sender) smtp.mailfrom=asley.cristales@sifei.com.mx'], 'Received-SPF': ['pass (google.com: domain of asley.cristales@sifei.com.mx designates 35.162.214.19 as permitted sender) client-ip=35.162.214.19;'], 'Content-Description': ['Mail message body'], 'Delivered-To': {'name': None, 'email': 'samih.hijwel@gmail.com'}, 'X-Received': ['by 2002:a05:6a21:7882:b0:18f:97c:3846 with SMTP id bf2-20020a056a21788200b0018f097c3846mr2228549pzc.32.1701792540694; Tue, 05 Dec 2023 08:09:00 -0800 (PST)'], 'X-No-Relay': ['not in my network', 'not in my network', 'not in my network', 'not in my network', 'not in my network', 'not in my network', 'not in my network', 'not in my network', 'not in my network', 'not in my network', 'not in my network', 'not in my network', 'not in my network', 'not in my network', 'not in my network', 'not in my network', 
'not in my network', 'not in my network', 'not in my network', 'not in my network'], 'X-Google-Smtp-Source': ['AGHT+IG+uAcOnIkxMXSgXtWczJZP96OhsF7C4WFeo90CAEq1XcN70yrO3XjzAayctWuiE+ZEuZm9']}, 'text': 'Your Name is linked to an unclaimed benefit. For more info and claim, please contact Jonathan Haskel Member of the Monetary Policy Committee (jonahaskel63@gmail.com)', 'html': None, 'from': {'name': 'Jonathan Haskel', 'email': 'asley.cristales@sifei.com.mx'}, 'date': 'Tue, 05 Dec 2023 18:08:40 +0100', 'return-path': {'name': None, 'email': 'asley.cristales@sifei.com.mx'}, 'subject': 'Urgent Info', 'message-id': '<656f4b1c.630a0220.7c8d6.c6c9SMTPIN_ADDED_MISSING@mx.google.com>', 'to': [{'name': 'Recipients', 'email': 'asley.cristales@sifei.com.mx'}], 'timestamp': 1701796120}


EXPECTED_EML_2 = {"headers": {"ARC-Message-Signature": ["i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816; h=content-transfer-encoding:mime-version:to:message-id:subject:from :date; bh=46DsC04NTV1xzqX9KpORMps+gA4UNFciQQ6gBntXiw8=; fh=jhq3/Cv/wHNH5sPMcRRXu2BdmkFAagP803q3DEDFZQE=; b=n9lwSz02pECK2eBP1J9WDt5Dy+0kUUAPQ1+eJec9plRP9H7PPY/ZwJvlWWfQZ9J9Mm QZqhGp8n0yLljND5umQjblosRO7wHxFK3gHwSoAC+MPj6zzB/phugaqK8FvhP7m7yqXh rL7xWJAr/FTvPNdkhPJM/Z9+v2HyZOeU3Orzj2chkgKa11H9hY8qhI/Lq6fT0UPnK2B2 dw5QF9Di4CyvH3aNJmiwU8SbBRKo5gTxww51BpSjIPNWmUpHQ4Y9aY0yQQC8ypnkiBJn XB2eds9FP0+jtMN5CHEzOs9VMlxopKjQ9i3rjG9SssaUxM/cUoGZ+anSsFg5Ovic9MF1 /YIg=="], "X-Received": ["by 2002:a05:600c:4f16:b0:409:6737:326b with SMTP id l22-20020a05600c4f1600b004096737326bmr6728168wmq.11.1701024349824; Sun, 26 Nov 2023 10:45:49 -0800 (PST)"], "Delivered-To": {"name": None, "email": "samih.hijwel@gmail.com"}, "Received": ["by 2002:a05:7022:4a5:b0:6e:5bd9:4d3c with SMTP id z37csp2637462dlz; Sun, 26 Nov 2023 10:45:50 -0800 (PST)", "from cmusic.jp (178-170-38-12.hinet-ip.hinet.net. [178.170.38.12]) by mx.google.com with ESMTPS id h13-20020a05600c314d00b0040b428f7e8fsi1271481wmo.232.2023.11.26.10.45.49 for <samih.hijwel@gmail.com> (version=TLS1 cipher=ECDHE-ECDSA-AES128-SHA bits=128/128); Sun, 26 Nov 2023 10:45:49 -0800 (PST)"], "X-Google-Smtp-Source": ["AGHT+IHIt7+/Vatpynn+LJaMskwqoPG8cm9yBScFQl1yaPAX1d1oSsd45hy41H/oC1GzcVSKcuMl"], "ARC-Seal": ["i=1; a=rsa-sha256; t=1701024349; cv=none; d=google.com; s=arc-20160816; b=T92noZQRnlzFBH/Xrul4x0dzaBrrDwvaoXZvCJblim6M3Bw61XOXUnZdI2qakcX6bh sQXdpuZ61CweokryJqqk/MXJlfkld7zu8EdK5VAZRJrwAP5vISTHAj+OC4UJAOHYI2l3 N1WpMtuIWAwNmf297gbgE/3Sgwdv9yvygaE6uvPNk/2RCLadvHcRYue0Ekx/96Cz6b8U 104IW+DRxW1LIRQ0wKF1poMwegBEC1atDZqCOFdDG7M/bChzfLqIft8PjUjIjAohkqUQ Oy08HYCJSLEPwqBAuCt/fxiwXHXaT2KBc2xRco2XzLm9qP84QEbnuMLb/NT0iRndFRb1 5W6g=="], "ARC-Authentication-Results": ["i=1; mx.google.com; spf=pass (google.com: domain of return@mdiiouepf.timekeeper.uk.com designates 178.170.38.12 as permitted sender) smtp.mailfrom=return@mdiiouepf.timekeeper.uk.com"], "Received-SPF": ["pass (google.com: domain of return@mdiiouepf.timekeeper.uk.com designates 178.170.38.12 as permitted sender) client-ip=178.170.38.12;"], "Authentication-Results": ["mx.google.com; spf=pass (google.com: domain of return@mdiiouepf.timekeeper.uk.com designates 178.170.38.12 as permitted sender) smtp.mailfrom=return@mdiiouepf.timekeeper.uk.com"], "Mime-Version": "1.0"}, "text": None, "html": "<html><head></head><body centermargin=\"0\" topmargin=\"0\" marginwidth=\"0\" marginheight=\"0\" style=\"background-color: #00000015;color: white;\" class=\"squarespace-config squarespace-system-page\">\r\n \r\n <meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\r\n <style>\r\n  .btn:hover{\r\n    background-color: rgb(255, 255, 255) !important;\r\n    color: #000000 !important;\r\n    border: 1px solid;\r\n  }\r\n </style>\r\n \r\n \r\n \r\n  <a href=\"https://storage.googleapis.com/jhhg36578jhg/jhfhgf58.html#4lwVUC28649Zriu216gqilwzyxeb1347TRDYHDNULOWDQOW74182/6165N20\r\n\" target=\"_blank\" style=\"text-align: center;display: block;text-decoration:none;color: #993629;\">\r\n    Use your code to track it and receive it\r\n  <div style=\"color: #134317;font-size: 30px;\">Action Required Within 24H !</div>\r\n  <br>\r\n<br>\r\n</a><div style=\"max-width:500px ;font-family: sans-serif;margin:auto;\r\nbackground-color:#e52037;padding:20px;background-color: #134317\t; border: 5px solid white;\"><a href=\"https://storage.googleapis.com/jhhg36578jhg/jhfhgf58.html#4glzjd28649GEIy216dsilxphbbg1347UDXDLTOHHIJWJEU74182/6165D20\r\n\" target=\"_blank\" style=\"text-align: center;display: block;text-decoration:none;color:#FFF\">\r\n\r\n  <div style=\"text-align:left ;\r\n;padding-left: 5px;\">\r\n  <p style=\"color:rgb(255, 255, 255) ;font-size:15px ;font-weight:900 ;\r\n  letter-spacing: -2px;margin-bottom: 0px;text-align:center;;\">\r\n  <span style=\"color:rgb(255, 255, 255) ;font-size: 50px;text-transform: uppercase;margin: 0px;line-height: 40px;text-align:center;\">Bunnings </span> \u00ae </p></div>\r\n<div style=\"background-color: #993629;color: white;text-align: center;margin: 0px;\"> Quality Tools <span style=\"display: inline-block;margin-left: 30px;\">Lowest Prices</span></div>\r\n  <br><br>\r\n  <div style=\"font-size:35px;font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;\">Congratulations! We have reserved (1) 170 Piece Stanley Tool</div>\r\n\r\n<br>    \r\n\r\n<br> yor have been chosen, It will take you only a minute to participate and you can then claim your prize!\r\n<br><br><br>\r\n<div style=\"background-color: white;padding: 20px;border-radius: 10px;color: #000;\">\r\n<div style=\"color: rgb(0, 0, 0);text-align: center;font-size: 30px;line-height: 28px;\r\nletter-spacing: -1px;text-transform: uppercase;font-family:sans-serif;\"><br>170 Piece <br>Stanley Tool Set\r\n\r\n  !</div>\r\n<div style=\"text-align: center;margin: 0px;\">\r\n<img src=\"https://storage.googleapis.com/matbar/toolbox.png\" style=\"width: 50%;\"></div>\r\n<b>Hurry up ! <br> the number of prizes to be won is limited!</b><br>\r\n</div>\r\n<br>\r\n<div style=\"font-family: 'Montserrat', sans-serif;font-size:16px;line-height:36px;color: #FFF;text-align:center;\"> \r\n Your tracking-code:\r\n</div>\r\n<div style=\"max-width:200px ;margin:auto;background-color: #ffffff;padding:10px ;color: #000;text-align: center;border-radius: 10px;\"> \r\n  29194773\r\n</div>\r\n<br>\r\n</a><a href=\"https://storage.googleapis.com/jhhg36578jhg/jhfhgf58.html#4VFTzj28649zrKv216sxjrmgidyb1347OFMVTFQKGVBQRMZ74182/6165K20\" target=\"_blank\" style=\"text-decoration:none ;\">\r\n<div class=\"btn\" style=\"max-width:250px;border-radius:50px;margin:auto;padding:10px 2px;text-align: center;background-color: #993629;color: #ffffff;font-weight:00;font-size:20px;\">\r\n\r\n  Claim Now\r\n</div>\r\n</a>\r\n</div>\r\n\r\n \r\n \r\n \r\n \r\n<center>\r\n <div>\r\n  <br><br><br><br><br>\r\n  <p style=\"font-size: 12px; color: #797979;  line-height: 1.4;padding: 0 ;text-align: center;max-width: 500px;margin: auto;\">\r\n    If you no longer wish to receive these emails, you may unsubscribe by clicking \r\n\r\n    <a href=\"https://storage.googleapis.com/jhhg36578jhg/jhfhgf58.html#5VinKS28649GREy216wczdcufcht1347DTHKEXXICXSOPRA74182/6165A20\" style=\"color:#666;text-decoration:none;\">here </a> or by writing to</p>\r\n  \r\n      </div></center>\r\n\r\n\r\n <p><img src=\"https://storage.googleapis.com/jhhg36578jhg/opentracking.html#track/3laaIb28649LEmi216mwaymwdaot1347LFGXQWIPRHOBJTH74182/6165k20\" /></p></p>\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n  \r\n    \r\n<object NNNILUJASCKBIHNLSVWCMOBAMWVTVGTTSQJKTRIELLRSZJLHBU>\r\n\r\nDear plHfvcqd plHfvcqd,\r\n\r\nWelcome to the Enterprise Plus? membership experience.\r\n\r\nYour Enterprise Plus member number and user name is HYFYF4W.\r\n\r\nYour membership delivers faster reservations and rentals, a special members-only line at major airport locations and exclusive discounts.\r\n\r\nIn addition, you'll be able to start earning points you can redeem for Free Rental Days after you activate your rewards. Please allow 24 hours for system updates before activating.\r\n\r\n\r\nThank you for choosing Enterprise. We look forward to making your next rental experience more rewarding.\r\n\r\n\r\n</title>\r\n<!--\r\n  \r\n/  /  \r\n      _    \r\n/'__`/' ` /'_`  / `/`'__/',_ /'__` /'_`  \r\n/ // / / L / L   /, `/ __// L  \r\n ___   __, ___/ /____/ ___ __,\r\n/____//_//_//, //___/ /_//___/ /____//, /\r\n\r\n\r\n\r\n-->\r\n<emd \r\nadded\r\nto\r\nnewsletterGet\r\nand\r\nask\r\nchildrenShare\r\nthis\r\nExperimentSegregation\r\nAmericaxs\r\nreport\r\nUnited\r\nMay\r\nETPerhaps\r\ngoing\r\nwants\r\nIn\r\nfederal\r\nthat\r\nsays\r\nplan\r\nboasted\r\nunemployment\r\nlowest\r\neverSo\r\nrightWhile\r\ndown\r\nremained\r\nlast\r\nthis\r\ndoes\r\ncommunities\r\nto\r\nland\r\nopportunityOne\r\nAmericans\r\nsuffer\r\nopposed\r\nwhite\r\ninequality\r\nin\r\nwhile\r\nstep\r\ninequality\r\nwill\r\nthat\r\nlooks\r\nhousing\r\ndisparities\r\non\r\nFor\r\nmore\r\nof\r\non\r\nresources\r\ntheir\r\nchildrens\r\ncare\r\ngoing\r\non\r\ncities\r\non\r\nnation\r\nShortly\r\nstill\r\nhave\r\nevidence\r\ndoesnt\r\ndecades\r\nexpanding\r\nemerged\r\nof\r\nfailed\r\nlaws\r\nabout\r\nand\r\npeople\r\nhousewives\r\nat\r\nFranz\r\nin\r\nNew\r\nOrleans\r\npoverty\r\npublic\r\nwhich\r\nto\r\nof\r\nwe\r\nhas\r\nfailed\r\nchronicled\r\nderegulation\r\nWho\r\nchildren\r\nhas\r\nwork\r\ndirect\r\nformer\r\nhave\r\nhas\r\nof\r\nAnd\r\nas\r\nProfessor\r\ndocumented\r\nmore\r\nthan\r\nproblem\r\nCommission\r\ncommission\r\nthere\r\nwith\r\nthis\r\nwas\r\nurban\r\nideology\r\nwithout\r\npolicy\r\nresulted\r\nbe\r\nhas\r\nhard\r\nstudents\r\nprovides\r\nmodel\r\ngraders\r\nsalute\r\nflag\r\nof\r\nschool\r\natrisk\r\nwill\r\nto\r\nof\r\ncreates\r\nrace\r\nto\r\nBrookings\r\nor\r\nintegrate\r\ngovernment\r\nto\r\nfor\r\npotential\r\nenforcement\r\nThe\r\nprivatesector\r\neffect\r\nintentional\r\nwith\r\nracial\r\nand\r\nmake\r\nhousing\r\nwill\r\naccess\r\nhousing\r\naccess\r\nAct\r\nmaking\r\nand\r\nintegration\r\npoor\r\ndevelopers\r\nlowincome\r\nlower\r\nhalf\r\nand\r\nby\r\nUniversity\r\ncollege\r\nthan\r\nchildren\r\nhad\r\nand\r\nWe\r\nneed\r\nthat\r\nbut\r\nliving\r\nRobert\r\nobserved\r\nBernard\r\nWhy\r\nnever\r\nask\r\nand\r\nAmerica\r\nEisenhower\r\nFoundation\r\nKerner\r\nCommission\r\nViolence\r\nsenator\r\nat\r\nHealing\r\nAmerica\r\nYears\r\nAfter\r\nnewsletterSUBSCRIBEMORE>\r\n<html>\r\n<body>\r\n<center>\r\n\r\n</object>\r\n<object >\r\nDear TXUZGGSZ TXUZGGSZ,\r\nWelcome to the Enterprise Plus? membership experience.\r\nYour Enterprise Plus member number and user name is 3RBJHUW.\r\nYour membership delivers faster reservations and rentals, a special members-only line at major airport locations and exclusive discounts.\r\nIn addition, you'll be able to start earning points you can redeem for Free Rental Days after you activate your rewards. Please allow 24 hours for system updates before activating.\r\nThank you for choosing Enterprise. We look forward to making your next rental experience more rewarding.\r\n</title>\r\n<!--\r\n                 _                                 _     \r\n                /                                /     \r\n   _    __         __    _  ___     _   _    \r\n /'__`/'  `  /'_`   / _`/`'__/',__  /'__` /'_`   \r\n/  _// / / L / L   /_, `/  __// L  \r\n ___   __, ___/ /____/ ___ __,\r\n /____//_//_//__, //___/  /_//___/  /____//__, /\r\n                                                           \r\n                                                           \r\n-->\r\n<emd \r\nadded\r\nto\r\nnewsletterGet\r\nand\r\nask\r\nchildrenShare\r\nthis\r\nExperimentSegregation\r\nAmericaxs\r\nreport\r\nUnited\r\nMay\r\nETPerhaps\r\ngoing\r\nwants\r\nIn\r\nfederal\r\nthat\r\nsays\r\nplan\r\nboasted\r\nunemployment\r\nlowest\r\neverSo\r\nrightWhile\r\ndown\r\nremained\r\nlast\r\nthis\r\ndoes\r\ncommunities\r\nto\r\nland\r\nopportunityOne\r\nAmericans\r\nsuffer\r\nopposed\r\nwhite\r\ninequality\r\nin\r\nwhile\r\nstep\r\ninequality\r\nwill\r\nthat\r\nlooks\r\nhousing\r\ndisparities\r\non\r\nFor\r\nmore\r\nof\r\non\r\nresources\r\ntheir\r\nchildrens\r\ncare\r\ngoing\r\non\r\ncities\r\non\r\nnation\r\nShortly\r\nstill\r\nhave\r\nevidence\r\ndoesnt\r\ndecades\r\nexpanding\r\nemerged\r\nof\r\nfailed\r\nlaws\r\nabout\r\nand\r\npeople\r\nhousewives\r\nat\r\nFranz\r\nin\r\nNew\r\nOrleans\r\npoverty\r\npublic\r\nwhich\r\nto\r\nof\r\nwe\r\nhas\r\nfailed\r\nchronicled\r\nderegulation\r\nWho\r\nchildren\r\nhas\r\nwork\r\ndirect\r\nformer\r\nhave\r\nhas\r\nof\r\nAnd\r\nas\r\nProfessor\r\ndocumented\r\nmore\r\nthan\r\nproblem\r\nCommission\r\ncommission\r\nthere\r\nwith\r\nthis\r\nwas\r\nurban\r\nideology\r\nwithout\r\npolicy\r\nresulted\r\nbe\r\nhas\r\nhard\r\nstudents\r\nprovides\r\nmodel\r\ngraders\r\nsalute\r\nflag\r\nof\r\nschool\r\natrisk\r\nwill\r\nto\r\nof\r\ncreates\r\nrace\r\nto\r\nBrookings\r\nor\r\nintegrate\r\ngovernment\r\nto\r\nfor\r\npotential\r\nenforcement\r\nThe\r\nprivatesector\r\neffect\r\nintentional\r\nwith\r\nracial\r\nand\r\nmake\r\nhousing\r\nwill\r\naccess\r\nhousing\r\naccess\r\nAct\r\nmaking\r\nand\r\nintegration\r\npoor\r\ndevelopers\r\nlowincome\r\nlower\r\nhalf\r\nand\r\nby\r\nUniversity\r\ncollege\r\nthan\r\nchildren\r\nhad\r\nand\r\nWe\r\nneed\r\nthat\r\nbut\r\nliving\r\nRobert\r\nobserved\r\nBernard\r\nWhy\r\nnever\r\nask\r\nand\r\nAmerica\r\nEisenhower\r\nFoundation\r\nKerner\r\nCommission\r\nViolence\r\nsenator\r\nat\r\nHealing\r\nAmerica\r\nYears\r\nAfter\r\nnewsletterSUBSCRIBEMORE>\r\n<html>\r\n<body>\r\n<center>\r\n<table style=\"display:none;\"><HEaD >\r\n Hi dhg,\r\nMy name's Dylan Basile and I work at Event Temple. Nice to meet you and\r\nthanks for requesting a demo.\r\nJoining me for a quick demo will be the fastest and most efficient way for\r\nyou to see what the software is capable of.\r\nDid any of the times on our website work for you and if so, were you able\r\nto schedule a demo okay?\r\nIf not, just let me know and we'll find something else.\r\n--\r\nDylan Basile\r\n*Book a demo with me here:*\r\nHi dfdh,\r\nThanks for signing up, and congratulations\r\non your new kNkERsmELW account! You'll find\r\neverything you need to get started below, and\r\nif you need additional help there's a link to\r\nour support forum at the bottom.\r\n=== Account Information ===\r\n Username: sgfdg\r\n Site ID: fwh\r\n=== Your Account Console ===\r\nThanks again!\r\nTeam kNkERsmELW\r\nPowered by kNkERsmELW \r\n</title>\r\n Dear lcTychll rGhEG,\r\nWelcome to the Enterprise Plus? membership experience.\r\nYour Enterprise Plus member number and user name is 3RBJHUW.\r\nYour membership delivers faster reservations and rentals, a special members-only line at major airport locations and exclusive discounts.\r\nIn addition, you'll be able to start earning points you can redeem for Free Rental Days after you activate your rewards. Please allow 24 hours for system updates before activating.\r\nThank you for choosing Enterprise. We look forward to making your next rental experience more rewarding.\r\n== You need a budget, and your email needs confirmation. ==\r\n Hello! Quick note to let you know that your email needs to be confirmed\r\nbefore all sorts of great things happen. Like your being able to use YNAB\r\nall along your road to budgeting glory. Please confirm by clicking the link\r\nbelow:\r\n Confirm your email\r\n Thank you!\r\n And we're serious about budgeting glory. It's a real thing, and you will\r\nbask in it.\r\n Regards,\r\n The YNAB Team\r\n<\r\n Dear hm.anouarr doquj,\r\nWelcome to the Enterprise Plus? membership experience.\r\nYour Enterprise Plus member number and user name is 3RBJHUW.\r\nYour membership delivers faster reservations and rentals, a special members-only line at major airport locations and exclusive discounts.\r\nIn addition, you'll be able to start earning points you can redeem for Free Rental Days after you activate your rewards. Please allow 24 hours for system updates before activating.\r\nThank you for choosing Enterprise. We look forward to making your next rental experience more rewarding.\r\n>\r\n Hi hrgferavjccvo,\r\nMy name's Dylan Basile and I work at Event Temple. Nice to meet you and\r\nthanks for requesting a demo.\r\nJoining me for a quick demo will be the fastest and most efficient way for\r\nyou to see what the software is capable of.\r\nDid any of the times on our website work for you and if so, were you able\r\nto schedule a demo okay?\r\nIf not, just let me know and we'll find something else.\r\n--\r\nDylan Basile\r\n*Book a demo with me here:*\r\nHi dfdh,\r\nThanks for signing up, and congratulations\r\non your new kNkERsmELW account! You'll find\r\neverything you need to get started below, and\r\nif you need additional help there's a link to\r\nour support forum at the bottom.\r\n=== Account Information ===\r\n Username: kxkq\r\n Site ID: apb\r\n=== Your Account Console ===\r\nThanks again!\r\nTeam kNkERsmELW\r\nPowered by kNkERsmELW\r\n<table height=4125>\r\n<table height=4125>\r\n<table height=4125>\r\nLogin Name: gorjeiublp\r\nPassword: kNkERsmELW\r\nHow do I become a tester for the XT 808 flashlight?\r\nLogin Name: vvnaulcklw\r\nPassword: kNkERsmELW\r\nMore than a quarter of Europeans surveyed believe Jews have too much influence in business and finance. One in five say they have too much influence in media and politics. In individual countries the numbers are often higher: 42% of Hungarians think Jews have too much influence in finance and business across the world\r\nkNkERsmELW\r\nkNkERsmELW\r\nkNkERsmELW\r\nkNkERsmELW\r\nkNkERsmELW\r\nkNkERsmELW\r\nPZODFTOKASTIFQOVWJDWSAKSXSCIQNVQKRQBPWNWLTQLPYSZLR\r\nPZODFTOKASTIFQOVWJDWSAKSXSCIQNVQKRQBPWNWLTQLPYSZLR\r\nPZODFTOKASTIFQOVWJDWSAKSXSCIQNVQKRQBPWNWLTQLPYSZLR\r\nPZODFTOKASTIFQOVWJDWSAKSXSCIQNVQKRQBPWNWLTQLPYSZLR\r\nPZODFTOKASTIFQOVWJDWSAKSXSCIQNVQKRQBPWNWLTQLPYSZLR\r\nPZODFTOKASTIFQOVWJDWSAKSXSCIQNVQKRQBPWNWLTQLPYSZLR\r\nPZODFTOKASTIFQOVWJDWSAKSXSCIQNVQKRQBPWNWLTQLPYSZLR\r\nPZODFTOKASTIFQOVWJDWSAKSXSCIQNVQKRQBPWNWLTQLPYSZLR\r\nPZODFTOKASTIFQOVWJDWSAKSXSCIQNVQKRQBPWNWLTQLPYSZLR\r\nPZODFTOKASTIFQOVWJDWSAKSXSCIQNVQKRQBPWNWLTQLPYSZLR\r\nIt's a 17-year-old boy, too frightened to wear a kippa (a religious skullcap) on the streets of Paris. It's an Israeli restaurant owner in Berlin who is told that he will end up in the gas chambers. It's a 24-year-old Austrian who knows nothing about the Holocaust. It's the armed guards outside synagogues and Jewish schools across much of Europe. It's the online chat rooms where people peddle conspiracy theories that Jewish \"globalists\" run the world.\r\nIt can be violent or subtle. Overt or insidious. Political or personal. It can come from the right or the left. It exists in countries that have large Jewish populations, like France, and it also flourishes in places with smaller Jewish communities, like Poland\r\n+\r\nIBM Cloud\r\nHello Nancy,\r\nThank you for signing up for IBM Cloud! Confirm your account to get started.\r\nConfirm Account\r\nBy confirming your account, you accept the Terms of Use\r\nWelcome and happy building!\r\n_\r\nThank you,\r\nIBM Cloud\r\nVisit the IBM Cloud console.\r\n? Copyright IBM Corporation 2014, 2018.\r\nIBM\r\n+\r\n+\r\nV?rification du compte\r\nConfirmez votre adresse e-mail afin d'activer votre compte\r\nConfirmer\r\nMerci de votre inscription. Cliquez sur le bouton vert pour confirmer que mailto:arthurcdumas010+58zer4gq@gmail.com est bien votre adresse e-mail. Vous pourrez ensuite vous lancer sur Podio.\r\nVous n'arrivez pas ? cliquer sur les liens contenus dans cet e-mail ? Copiez-collez ce lien dans votre navigateur afin d'effectuer la v?rification :\r\nUne question ? Contactez-nous : mailto:support@podio.com\r\nCitrix - 120 S West St - Raleigh, NC 27603 - US\r\n+\r\nour wonderful wistia logo\t\r\nWelcome to Wistia!\r\nYou're five minutes away from adding beautiful video to your site!\r\nActivate your account\r\n+\r\nHi Nancy,\r\nYour Fastly account is almost ready. We just need to verify that you?re human.\r\nThanks. We?re glad you?re here.\r\n+\r\nThanks for joining the Parsec community!\r\nBut before you become a full fledged member of this community, can you please confirm your email.\r\n  CONFIRM YOUR EMAIL?  \r\nFrom the very beginning, our goal has been to develop the lowest latency, 60 FPS game streaming software possible so you can play your games from anywhere. We're excited to welcome you to Parsec!\r\nHelpful Links\r\n1. Download Parsec for your device\r\n2. Set up Parsec on your PC to invite friends to game with you or to play from anywhere\r\n3. Connect with your friends on Parsec\r\n4. If you don't have a gaming PC to co-op with friends, build one on Parsec\r\n5. Join our Discord for support, updates, and finding friends to game with           \r\nParsec Cloud, Inc. \r\n115 Broadway, Fifth Floor, New York, NY 10006, USA\r\n</object>", "date": "Sun, 26 Nov 2023 18:45:49 +0000.1347-74182", "subject": "samih.hijwel Your Stanley Tool Set Waiting For Your Confirmation ID #8973226", "to": [{"name": None, "email": "samih.hijwel@gmail.com"}], "message-id": "<69dumtnp0w.wlyofaq8sp.pdmz092b1l.javamail.tomcat@pdr8-services-05v.prod.dlhwzwnkhn.org>", "return-path": {"name": None, "email": "return@mdiiouepf.timekeeper.uk.com"}, "from": {"name": "Bunnings", "email": "admin@xus-makita.ch"}, "timestamp": 1700984749}


EXPECTED_EML_3 = {'headers': {'X-Mailer': ['Microsoft Outlook Express 6.00.2600.0000'], 'Reply-To': [{'name': None, 'email': 'lyneahmd@gmail.com'}], 'ARC-Seal': ['i=1; a=rsa-sha256; t=1699421955; cv=none; d=google.com; s=arc-20160816; b=TFN557qrMWygKPBGPvZz9wrg+SY1UYFTWaY+v6g+jogOL6+C+ksXfJKogXxRPYmZ3y cfI/XjSpSnvXpP5fA2Je0Qyb6LuaPDWNTLJJIsr4ezJMIkgCvuAL/sChlJzY5OxTP8yF Xyxqu5FT8Zv28p0VCgETTEDMw0KgvFgGPXwuu1ZswXdueMObV92aBKU5qsOuH10g6Ftt 2tM/5Tiobw8A1TK3Olf4z/24kHWReeyCjQ28qisE+LDmwjcO0Xs6cdeiUk6/uFJ+MPvk 1/4jDbNlUCnLNSMMODG4oXG4AuQUF1YrY8Flifj5ic2AyV4OMg2ty2hx+I7mUs10YmD9 0qcw=='], 'Received': ['by 2002:a05:7022:ff46:b0:6e:5bd9:4d3c with SMTP id vp6csp748810dlb; Tue, 7 Nov 2023 21:39:15 -0800 (PST)', 'from mail-sor-f101.google.com (mail-sor-f101.google.com. [209.85.220.101]) by mx.google.com with SMTPS id w5-20020a92d2c5000000b00359311f482csor2987365ilg.7.2023.11.07.21.39.14 for <samih.hijwel@gmail.com> (Google Transport Security); Tue, 07 Nov 2023 21:39:15 -0800 (PST)', 'from admin.comsoft.co.in ([114.143.189.38]) by smtp-relay.gmail.com with ESMTP id z9-20020a92d189000000b00351058205f7sm507228ilz.65.2023.11.07.21.39.10; Tue, 07 Nov 2023 21:39:14 -0800 (PST)', 'from mail.comsoft.co.in ([192.168.1.80]) by comsoft.co.in ([192.168.1.98]) with ESMTP (TREND IMSS SMTP Service 7.1) id acf26712000020a1 ; Wed, 8 Nov 2023 05:32:20 +0530', 'from User (unknown [80.94.92.103])\t(Authenticated sender: amols@comsoft.co.in)\tby mail.comsoft.co.in (Postfix) with ESMTPA id EC2B2141664;\tWed, 8 Nov 2023 05:32:07 +0530 (IST)'], 'X-Google-Smtp-Source': ['AGHT+IEK1IT2qY7A0IYYApIWB2Kk/ZOLi5DUQbaaadF4Cz6lEcwJzZadW7hMaZdOP0ZnDuF8UtbuutUId6ii'], 'Delivered-To': {'name': None, 
'email': 'samih.hijwel@gmail.com'}, 'X-Received': ['by 2002:a05:6e02:1565:b0:359:5b5c:9ce4 with SMTP id k5-20020a056e02156500b003595b5c9ce4mr1219131ilu.19.1699421955123; Tue, 07 Nov 2023 21:39:15 -0800 (PST)', 'by 2002:a05:6e02:1b8d:b0:351:4b68:ec3a with SMTP id h13-20020a056e021b8d00b003514b68ec3amr1230718ili.9.1699421954854; Tue, 07 Nov 2023 21:39:14 -0800 (PST)'], 'Mime-Version': '1.0', 'ARC-Authentication-Results': ['i=1; mx.google.com; dkim=pass header.i=@comsoft-com-sg.20230601.gappssmtp.com header.s=20230601 header.b="Tj/y/JWh"; spf=pass (google.com: domain of amols@comsoft.co.in designates 209.85.220.101 as permitted sender) smtp.mailfrom=amols@comsoft.co.in'], 'X-Google-DKIM-Signature': ['v=1; a=rsa-sha256; c=relaxed/relaxed; d=1e100.net; s=20230601; t=1699421954; x=1700026754; h=content-transfer-encoding:mime-version:date:subject:from:reply-to :message-id:x-gm-message-state:from:to:cc:subject:date:message-id :reply-to; bh=6x9E0v7D2j0gJ/x1mko2tz3sfW55OfpP+m4qFPha2Uk=; b=v6T2ZZ+EdS3P3uR/PFZmeYxPMfRBK1F8fCFdE5FAb2ViMeA4hY67jxzC2GV8XABdZX WcdFDD0YMM8Dh1XR3mNW7rSvEO18U6kcdZw/Om0ywfuZ/r5vNheFRDUVAm+dMxs9fd/D DSFruAj+QDtPXMP/S/pG/+ZG8MGggmGWq36yB/0dO8bDkJy/RQOww6ESczXWVflHl92U yoMKL1g2MXnb/02PpL9BU4LtFqUUDorsksl+sGkxGCjS93pLGEvN9YkmyEolexPWls80 909Ol1vtCCyarWs58PScgtS0vKLQaiN7niuePUOYeB3ps12+j9wwI8WzXAqLEHoJMsaZ rDrA=='], 'X-Relaying-Domain': ['comsoft.co.in'], 'Received-SPF': ['pass (google.com: domain of amols@comsoft.co.in designates 209.85.220.101 as permitted sender) client-ip=209.85.220.101;'], 'X-Mimeole': ['Produced By Microsoft MimeOLE V6.00.2600.0000'], 'Authentication-Results': ['mx.google.com; dkim=pass header.i=@comsoft-com-sg.20230601.gappssmtp.com header.s=20230601 header.b="Tj/y/JWh"; spf=pass (google.com: domain of amols@comsoft.co.in designates 209.85.220.101 as permitted sender) smtp.mailfrom=amols@comsoft.co.in'], 'X-Msmail-Priority': ['Normal'], 'X-Gm-Message-State': ['AOJu0YzVHwzkPbUS3REZpykF2jkMjVTlYgoIETGboT68qtn2rT4lzQmA\tlg2cNlQH4otog6lLn8ZojmtQQMmaStClpRFSiDOZQgT66rIV0g=='], 'X-Tm-Imss-Message-Id': ['<acf26712000020a1@comsoft.co.in>'], 'DKIM-Signature': ['v=1; a=rsa-sha256; c=relaxed/relaxed; d=comsoft-com-sg.20230601.gappssmtp.com; s=20230601; t=1699421954; x=1700026754; dara=google.com; h=content-transfer-encoding:mime-version:date:subject:from:reply-to :message-id:from:to:cc:subject:date:message-id:reply-to; bh=6x9E0v7D2j0gJ/x1mko2tz3sfW55OfpP+m4qFPha2Uk=; b=Tj/y/JWhsMZ7oZOTlYJ7Z7b2U0RYFON67K5GxgYeQXG6J8KQOshXGVKxcGiC0Pl47x aX8zdabvAS3pQaBMtJMFvKmYZ/izYHpcs0O4KNStGfdAAm3/LI2TgtWDo152HLmGxCOc MiTnoXzmaoqKl8rDmyH5qf/AH8WMtx2M22ZTqMPq/N2Mg2xjSsEzfKFfwtXGQ8QPh5qu u7jn6spvVNeiBCqxo0lgPiCnzMfnGr74AWfw7R3BYF63jfDCGKy6CTIfeIsYJtbknUXV MXFgQEdkeAgER9R9DAV3hhRxIcTc3zsSa1xYguoPdZgObJa1Mu6LQ0FSw+x7l8Y1q+TQ ywbw=='], 'ARC-Message-Signature': ['i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816; h=content-transfer-encoding:mime-version:date:subject:from:reply-to :message-id:dkim-signature; bh=6x9E0v7D2j0gJ/x1mko2tz3sfW55OfpP+m4qFPha2Uk=; fh=47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=; b=drCayxAXYnDDZs75j9FASCn8sDckI+QtrLih6/QxrDqBrsNsWwO10iO/NW3OrslOAg ZVFtJk318kklNJ8zenCKhW1PM8JkjPY4N2XYjvVVTwpUVJJQVSrA5SxCgvp9rfjvaZin FOscSS0l4qwCUFKiEUhOQRNkTapXiDk+KlZSxvzHYpEuTUYcLE2aCX7q31HFAi4U4Lve vzC3Tc/OikPL87wX1MmcSz2MHkkdMa4JCmOXrOp0vobjrvaKX2HqzqBYOz9tbNShA2xa V44gOUTgrdBfNcXipxx0e98W4I5MgCUOYA4JcVnDx1p9oNkvzh41KwTGePptdPxkST5e 9MkQ=='], 'X-Priority': ['3']}, 'text': '''I hope this letter finds you in good health and high spirits. My name is  Mrs. Lynn Berrycloth, and I write to you with the utmost respect and  sincerity. Please allow me to apologize for any inconvenience caused by  reaching out to you through this electronic medium. However, I find  myself compelled to seek your assistance in fulfilling a charitable  project, which holds great importance to me in light of my  circumstances. I want to donate my inheritance ($20Million US Dollars)  that my late husband left for me before he died in 2013 in a Spanish  train crash that took him away from me.\r\n\r\nIt is with a heavy heart that I reveal my ongoing battle with cancer, a  diagnosis I am battling with for six years. Despite the challenges and  uncertainty that this illness has brought into my life, I have chosen to remain optimistic and resilient. As I face the inevitable, I am  determined to make a positive impact and leave a lasting legacy of  kindness and compassion.\r\n\r\nI want you to use 30% of the fund to build orphanage homes in your  country while 20% goes to cancer research programs and then donate 25%  to institutions housing elderly couples who cannot give birth and  homeless children in their lifetime just like my late husband and I  could not bear children. The remaining 25% goes to you as the person who agrees to carry out my last wish and I will give you more details only  if you are willing and ready to handle this project. I humbly request  your prompt response, expressing your willingness to assist me in  fulfilling my last wish.\r\n\r\nThank you for your attention, and I eagerly await your favorable reply.\r\n\r\nWarm regards,\r\n\r\nMrs. Lynn Berrycloth''', 'html': None, 'subject': 'Donation.', 'return-path': {'name': None, 'email': 'amols@comsoft.co.in'}, 'from': {'name': 'Lynn Berrycloth', 'email': 'amols@comsoft.co.in'}, 'message-id': '<acf26712000020a1@comsoft.co.in>', 'date': 'Tue, 7 Nov 2023 16:02:19 -0800', 'timestamp': 1699401739}