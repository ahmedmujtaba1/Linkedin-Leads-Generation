from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import smtplib

sender_email = "saadmohsinparoopia@gmail.com"
rec_email = "rustomdeveloper@gmail.com"
password = "ghzvtrbjgeeqynox"
subject = "Unlock the Power of Innovative Solutions with Our Services 🚀"

message = MIMEMultipart("alternative")
message["From"] = sender_email
message["To"] = rec_email
message["Subject"] = Header(subject, "utf-8")

html_content = f"""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">
<script src="chrome-extension://eppiocemhmnlbhjplcgkofciiegomcon/libs/extend-native-history-api.js"></script>

<head>
    <meta charset="UTF-8">
    <meta content="width=device-width, initial-scale=1" name="viewport">
    <meta name="x-apple-disable-message-reformatting">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta content="telephone=no" name="format-detection">
    <title></title>
    <!--[if (mso 16)]>
    <style type="text/css">
    a {{text-decoration: none;}}
    </style>
    <![endif]-->
    <!--[if gte mso 9]><style>sup {{ font-size: 100% !important; }}</style><![endif]-->
    <!--[if gte mso 9]>
<xml>
    <o:OfficeDocumentSettings>
    <o:AllowPNG></o:AllowPNG>
    <o:PixelsPerInch>96</o:PixelsPerInch>
    </o:OfficeDocumentSettings>
</xml>
<![endif]-->
    <!--[if !mso]><!-- -->
    <link href="https://fonts.googleapis.com/css2?family=Alegreya&display=swap" rel="stylesheet">
    <!--<![endif]-->
</head>

<style>

    /* CONFIG STYLES Please do not delete and edit CSS styles below */
/* IMPORTANT THIS STYLES MUST BE ON FINAL EMAIL */
#outlook a {{
    padding: 0;
}}

.es-button {{
    mso-style-priority: 100 !important;
    text-decoration: none !important;
}}

a[x-apple-data-detectors] {{
    color: inherit !important;
    text-decoration: none !important;
    font-size: inherit !important;
    font-family: inherit !important;
    font-weight: inherit !important;
    line-height: inherit !important;
}}

.es-desk-hidden {{
    display: none;
    float: left;
    overflow: hidden;
    width: 0;
    max-height: 0;
    line-height: 0;
    mso-hide: all;
}}

/*
END OF IMPORTANT
*/
body {{
    width: 100%;
    font-family: Alegreya, serif;
    -webkit-text-size-adjust: 100%;
    -ms-text-size-adjust: 100%;
}}

table {{
    mso-table-lspace: 0pt;
    mso-table-rspace: 0pt;
    border-collapse: collapse;
    border-spacing: 0px;
}}

table td,
body,
.es-wrapper {{
    padding: 0;
    Margin: 0;
}}

.es-content,
.es-header,
.es-footer {{
    table-layout: fixed !important;
    width: 100%;
}}

img {{
    display: block;
    border: 0;
    outline: none;
    text-decoration: none;
    -ms-interpolation-mode: bicubic;
}}

p,
hr {{
    Margin: 0;
}}

h1,
h2,
h3,
h4,
h5 {{
    Margin: 0;
    line-height: 120%;
    mso-line-height-rule: exactly;
    font-family: Alegreya, serif;
}}

p,
ul li,
ol li,
a {{
    -webkit-text-size-adjust: none;
    -ms-text-size-adjust: none;
    mso-line-height-rule: exactly;
}}

.es-left {{
    float: left;
}}

.es-right {{
    float: right;
}}

.es-p5 {{
    padding: 5px;
}}

.es-p5t {{
    padding-top: 5px;
}}

.es-p5b {{
    padding-bottom: 5px;
}}

.es-p5l {{
    padding-left: 5px;
}}

.es-p5r {{
    padding-right: 5px;
}}

.es-p10 {{
    padding: 10px;
}}

.es-p10t {{
    padding-top: 10px;
}}

.es-p10b {{
    padding-bottom: 10px;
}}

.es-p10l {{
    padding-left: 10px;
}}

.es-p10r {{
    padding-right: 10px;
}}

.es-p15 {{
    padding: 15px;
}}

.es-p15t {{
    padding-top: 15px;
}}

.es-p15b {{
    padding-bottom: 15px;
}}

.es-p15l {{
    padding-left: 15px;
}}

.es-p15r {{
    padding-right: 15px;
}}

.es-p20 {{
    padding: 20px;
}}

.es-p20t {{
    padding-top: 20px;
}}

.es-p20b {{
    padding-bottom: 20px;
}}

.es-p20l {{
    padding-left: 20px;
}}

.es-p20r {{
    padding-right: 20px;
}}

.es-p25 {{
    padding: 25px;
}}

.es-p25t {{
    padding-top: 25px;
}}

.es-p25b {{
    padding-bottom: 25px;
}}

.es-p25l {{
    padding-left: 25px;
}}

.es-p25r {{
    padding-right: 25px;
}}

.es-p30 {{
    padding: 30px;
}}

.es-p30t {{
    padding-top: 30px;
}}

.es-p30b {{
    padding-bottom: 30px;
}}

.es-p30l {{
    padding-left: 30px;
}}

.es-p30r {{
    padding-right: 30px;
}}

.es-p35 {{
    padding: 35px;
}}

.es-p35t {{
    padding-top: 35px;
}}

.es-p35b {{
    padding-bottom: 35px;
}}

.es-p35l {{
    padding-left: 35px;
}}

.es-p35r {{
    padding-right: 35px;
}}

.es-p40 {{
    padding: 40px;
}}

.es-p40t {{
    padding-top: 40px;
}}

.es-p40b {{
    padding-bottom: 40px;
}}

.es-p40l {{
    padding-left: 40px;
}}

.es-p40r {{
    padding-right: 40px;
}}

.es-menu td {{
    border: 0;
}}

.es-menu td a img {{
    display: inline-block !important;
    vertical-align: middle;
}}

/*
END CONFIG STYLES
*/
s {{
    text-decoration: line-through;
}}

p,
ul li,
ol li {{
    font-family: Alegreya, serif;
    line-height: 150%;
}}

ul li,
ol li {{
    Margin-bottom: 15px;
    margin-left: 0;
}}

a {{
    text-decoration: underline;
}}

.es-menu td a {{
    text-decoration: none;
    display: block;
    font-family: Alegreya, serif;
}}

.es-wrapper {{
    width: 100%;
    height: 100%;
    background-repeat: repeat;
    background-position: center top;
}}

.es-wrapper-color,
.es-wrapper {{
    background-color: #ffffff;
}}

.es-header {{
    background-color: transparent;
    background-repeat: repeat;
    background-position: center top;
}}

.es-header-body {{
    background-color: #F7ECDE;
}}

.es-header-body p,
.es-header-body ul li,
.es-header-body ol li {{
    color: #203c3b;
    font-size: 16px;
}}

.es-header-body a {{
    color: #203c3b;
    font-size: 16px;
}}

.es-content-body {{
    background-color: #F7ECDE;
}}

.es-content-body p,
.es-content-body ul li,
.es-content-body ol li {{
    color: #203c3b;
    font-size: 18px;
}}

.es-content-body a {{
    color: #203c3b;
    font-size: 18px;
}}

.es-footer {{
    background-color: transparent;
    background-repeat: repeat;
    background-position: center top;
}}

.es-footer-body {{
    background-color: #E9DAC1;
}}

.es-footer-body p,
.es-footer-body ul li,
.es-footer-body ol li {{
    color: #203c3b;
    font-size: 14px;
}}

.es-footer-body a {{
    color: #203c3b;
    font-size: 14px;
}}

.es-infoblock,
.es-infoblock p,
.es-infoblock ul li,
.es-infoblock ol li {{
    line-height: 120%;
    font-size: 12px;
    color: #cccccc;
}}

.es-infoblock a {{
    font-size: 12px;
    color: #cccccc;
}}

h1 {{
    font-size: 30px;
    font-style: normal;
    font-weight: normal;
    color: #203c3b;
}}

h2 {{
    font-size: 24px;
    font-style: normal;
    font-weight: normal;
    color: #203c3b;
}}

h3 {{
    font-size: 20px;
    font-style: normal;
    font-weight: normal;
    color: #203c3b;
}}

.es-header-body h1 a,
.es-content-body h1 a,
.es-footer-body h1 a {{
    font-size: 30px;
}}

.es-header-body h2 a,
.es-content-body h2 a,
.es-footer-body h2 a {{
    font-size: 24px;
}}

.es-header-body h3 a,
.es-content-body h3 a,
.es-footer-body h3 a {{
    font-size: 20px;
}}

a.es-button,
button.es-button {{
    padding: 10px 30px 10px 30px;
    display: inline-block;
    background: #54BAB9;
    border-radius: 30px;
    font-size: 22px;
    font-family: Alegreya, serif;
    font-weight: normal;
    font-style: normal;
    line-height: 120%;
    color: #F7ECDE;
    text-decoration: none;
    width: auto;
    text-align: center;
    mso-padding-alt: 0;
    mso-border-alt: 10px solid #54BAB9;
}}

.es-button-border {{
    border-style: solid solid solid solid;
    border-color: #2cb543 #2cb543 #2cb543 #2cb543;
    background: #54BAB9;
    border-width: 0px 0px 0px 0px;
    display: inline-block;
    border-radius: 30px;
    width: auto;
}}

.msohide {{
    mso-hide: all;
}}

/* RESPONSIVE STYLES Please do not delete and edit CSS styles below. If you don't need responsive layout, please delete this section. */
@media only screen and (max-width: 600px) {{

    p,
    ul li,
    ol li,
    a {{
        line-height: 150% !important;
    }}

    h1,
    h2,
    h3,
    h1 a,
    h2 a,
    h3 a {{
        line-height: 120%;
    }}

    h1 {{
        font-size: 30px !important;
        text-align: center !important;
    }}

    h2 {{
        font-size: 24px !important;
        text-align: center !important;
    }}

    h3 {{
        font-size: 20px !important;
        text-align: center !important;
    }}

    .es-header-body h1 a,
    .es-content-body h1 a,
    .es-footer-body h1 a {{
        font-size: 30px !important;
        text-align: center !important;
    }}

    .es-header-body h2 a,
    .es-content-body h2 a,
    .es-footer-body h2 a {{
        font-size: 24px !important;
        text-align: center !important;
    }}

    .es-header-body h3 a,
    .es-content-body h3 a,
    .es-footer-body h3 a {{
        font-size: 20px !important;
        text-align: center !important;
    }}

    .es-menu td a {{
        font-size: 12px !important;
    }}

    .es-header-body p,
    .es-header-body ul li,
    .es-header-body ol li,
    .es-header-body a {{
        font-size: 14px !important;
    }}

    .es-content-body p,
    .es-content-body ul li,
    .es-content-body ol li,
    .es-content-body a {{
        font-size: 14px !important;
    }}

    .es-footer-body p,
    .es-footer-body ul li,
    .es-footer-body ol li,
    .es-footer-body a {{
        font-size: 12px !important;
    }}

    .es-infoblock p,
    .es-infoblock ul li,
    .es-infoblock ol li,
    .es-infoblock a {{
        font-size: 12px !important;
    }}

    *[class="gmail-fix"] {{
        display: none !important;
    }}

    .es-m-txt-c,
    .es-m-txt-c h1,
    .es-m-txt-c h2,
    .es-m-txt-c h3 {{
        text-align: center !important;
    }}

    .es-m-txt-r,
    .es-m-txt-r h1,
    .es-m-txt-r h2,
    .es-m-txt-r h3 {{
        text-align: right !important;
    }}

    .es-m-txt-l,
    .es-m-txt-l h1,
    .es-m-txt-l h2,
    .es-m-txt-l h3 {{
        text-align: left !important;
    }}

    .es-m-txt-r img,
    .es-m-txt-c img,
    .es-m-txt-l img {{
        display: inline !important;
    }}

    .es-button-border {{
        display: inline-block !important;
    }}

    a.es-button,
    button.es-button {{
        font-size: 18px !important;
        display: inline-block !important;
    }}

    .es-adaptive table,
    .es-left,
    .es-right {{
        width: 100% !important;
    }}

    .es-content table,
    .es-header table,
    .es-footer table,
    .es-content,
    .es-footer,
    .es-header {{
        width: 100% !important;
        max-width: 600px !important;
    }}

    .es-adapt-td {{
        display: block !important;
        width: 100% !important;
    }}

    .adapt-img {{
        width: 100% !important;
        height: auto !important;
    }}

    .es-m-p0 {{
        padding: 0 !important;
    }}

    .es-m-p0r {{
        padding-right: 0 !important;
    }}

    .es-m-p0l {{
        padding-left: 0 !important;
    }}

    .es-m-p0t {{
        padding-top: 0 !important;
    }}

    .es-m-p0b {{
        padding-bottom: 0 !important;
    }}

    .es-m-p20b {{
        padding-bottom: 20px !important;
    }}

    .es-mobile-hidden,
    .es-hidden {{
        display: none !important;
    }}

    tr.es-desk-hidden,
    td.es-desk-hidden,
    table.es-desk-hidden {{
        width: auto !important;
        overflow: visible !important;
        float: none !important;
        max-height: inherit !important;
        line-height: inherit !important;
    }}

    tr.es-desk-hidden {{
        display: table-row !important;
    }}

    table.es-desk-hidden {{
        display: table !important;
    }}

    td.es-desk-menu-hidden {{
        display: table-cell !important;
    }}

    .es-menu td {{
        width: 1% !important;
    }}

    table.es-table-not-adapt,
    .esd-block-html table {{
        width: auto !important;
    }}

    table.es-social {{
        display: inline-block !important;
    }}

    table.es-social td {{
        display: inline-block !important;
    }}

    .es-desk-hidden {{
        display: table-row !important;
        width: auto !important;
        overflow: visible !important;
        max-height: inherit !important;
    }}

    .es-m-p5 {{
        padding: 5px !important;
    }}

    .es-m-p5t {{
        padding-top: 5px !important;
    }}

    .es-m-p5b {{
        padding-bottom: 5px !important;
    }}

    .es-m-p5r {{
        padding-right: 5px !important;
    }}

    .es-m-p5l {{
        padding-left: 5px !important;
    }}

    .es-m-p10 {{
        padding: 10px !important;
    }}

    .es-m-p10t {{
        padding-top: 10px !important;
    }}

    .es-m-p10b {{
        padding-bottom: 10px !important;
    }}

    .es-m-p10r {{
        padding-right: 10px !important;
    }}

    .es-m-p10l {{
        padding-left: 10px !important;
    }}

    .es-m-p15 {{
        padding: 15px !important;
    }}

    .es-m-p15t {{
        padding-top: 15px !important;
    }}

    .es-m-p15b {{
        padding-bottom: 15px !important;
    }}

    .es-m-p15r {{
        padding-right: 15px !important;
    }}

    .es-m-p15l {{
        padding-left: 15px !important;
    }}

    .es-m-p20 {{
        padding: 20px !important;
    }}

    .es-m-p20t {{
        padding-top: 20px !important;
    }}

    .es-m-p20r {{
        padding-right: 20px !important;
    }}

    .es-m-p20l {{
        padding-left: 20px !important;
    }}

    .es-m-p25 {{
        padding: 25px !important;
    }}

    .es-m-p25t {{
        padding-top: 25px !important;
    }}

    .es-m-p25b {{
        padding-bottom: 25px !important;
    }}

    .es-m-p25r {{
        padding-right: 25px !important;
    }}

    .es-m-p25l {{
        padding-left: 25px !important;
    }}

    .es-m-p30 {{
        padding: 30px !important;
    }}

    .es-m-p30t {{
        padding-top: 30px !important;
    }}

    .es-m-p30b {{
        padding-bottom: 30px !important;
    }}

    .es-m-p30r {{
        padding-right: 30px !important;
    }}

    .es-m-p30l {{
        padding-left: 30px !important;
    }}

    .es-m-p35 {{
        padding: 35px !important;
    }}

    .es-m-p35t {{
        padding-top: 35px !important;
    }}

    .es-m-p35b {{
        padding-bottom: 35px !important;
    }}

    .es-m-p35r {{
        padding-right: 35px !important;
    }}

    .es-m-p35l {{
        padding-left: 35px !important;
    }}

    .es-m-p40 {{
        padding: 40px !important;
    }}

    .es-m-p40t {{
        padding-top: 40px !important;
    }}

    .es-m-p40b {{
        padding-bottom: 40px !important;
    }}

    .es-m-p40r {{
        padding-right: 40px !important;
    }}

    .es-m-p40l {{
        padding-left: 40px !important;
    }}
}}

/* END RESPONSIVE STYLES */
html,
body {{
    font-family: arial, 'helvetica neue', helvetica, sans-serif;
}}

.es-p-default {{
    padding-top: 20px;
    padding-right: 40px;
    padding-bottom: 0px;
    padding-left: 40px;
}}

.es-p-all-default {{
    padding: 0px;
}}

</style>

<body data-new-gr-c-s-loaded="14.1091.0" bis_status="ok">
    <div dir="ltr" class="es-wrapper-color">
        <!--[if gte mso 9]>
			<v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t">
				<v:fill type="tile" color="#ffffff"></v:fill>
			</v:background>
		<![endif]-->
        <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0">
            <tbody>
                <tr>
                    <td class="esd-email-paddings" valign="top">
                        <table class="es-content" cellspacing="0" cellpadding="0" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" align="center">
                                        <table class="es-content-body" width="600" cellspacing="0" cellpadding="0" align="center">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p20t es-p40r es-p40l" align="left" esd-custom-block-id="819266">
                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="es-m-p0r es-m-p20b esd-container-frame" width="520" valign="top" align="center">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-banner" style="position: relative;" esdev-config="h1"><a target="_blank" href=""><img class="adapt-img esdev-stretch-width esdev-banner-rendered" src="https://imgtr.ee/images/2023/12/16/43d744bae00ccbc532fa2bf36a02b869.png" alt title width="380" height="300" style="display: block;"></a></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="esd-structure es-p20t es-p40b es-p40r es-p40l" align="left">
                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="520" class="esd-container-frame" align="center" valign="top">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-p20t es-p20b">
                                                                                        <h1>Hey&nbsp;Lillian!</h1>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-p30b">
                                                                                        <p>I trust this message finds you well. We are reaching out to you with excitement, as we are eager to introduce our diverse range of services tailored to meet your technological needs.</p>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="esd-structure es-p40r es-m-p40l" align="left" esd-custom-block-id="819361" esdev-config="h5">
                                                        <!--[if mso]><table width="560" cellpadding="0" cellspacing="0"><tr><td width="300" valign="top"><![endif]-->
                                                        <table cellpadding="0" cellspacing="0" class="es-left" align="left">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="300" class="es-m-p20b esd-container-frame" align="left">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-image" style="font-size: 0px;"><a target="_blank" href="https://www.fiverr.com/mohsinharoon77/do-web-data-scraping-from-any-website-using-python-for-your-business"><img class="adapt-img p_image" src="https://imgtr.ee/images/2023/12/16/78d85fff3f113c9cf5bb4f87a0a79686.png" alt style="display: block;" width="300"></a></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td><td width="20"></td><td width="240" valign="top"><![endif]-->
                                                        <table cellpadding="0" cellspacing="0" class="es-right" align="right">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="240" align="left" class="esd-container-frame">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr class="es-mobile-hidden">
                                                                                    <td align="center" class="esd-block-spacer" height="130"></td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="" class="esd-block-text es-p5b" esd-links-underline="none">
                                                                                        <p> Gain a competitive edge by harnessing the power of web scraping. Extract valuable insights, monitor competitors, and stay ahead in the dynamic digital landscape.</p>
                                                                                        <h2><a target="_blank" style="text-decoration: none;" href="https://www.fiverr.com/mohsinharoon77/do-web-data-scraping-from-any-website-using-python-for-your-business">Order Our Web Scraping Service→</a></h2>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-spacer es-p20b es-p20r es-p20l" style="font-size:0">
                                                                                        <table border="0" width="70%" height="100%" cellpadding="0" cellspacing="0" style="width: 70% !important; display: inline-table;">
                                                                                            <tbody>
                                                                                                <tr>
                                                                                                    <td style="border-bottom: 3px solid #54bab9; background: unset; height: 1px; width: 100%; margin: 0px;"></td>
                                                                                                </tr>
                                                                                            </tbody>
                                                                                        </table>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="esd-structure es-p20l es-m-p40r es-m-p40l" align="left" esd-custom-block-id="819362" esdev-config="h6">
                                                        <!--[if mso]><table dir="ltr" cellpadding="0" cellspacing="0"><tr><td><table dir="rtl" width="580" cellpadding="0" cellspacing="0"><tr><td dir="ltr" width="300" valign="top"><![endif]-->
                                                        <table cellpadding="0" cellspacing="0" class="es-right" align="right">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="300" align="left" class="esd-container-frame es-m-p20b">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-image" style="font-size: 0px;"><a target="_blank" href="https://www.fiverr.com/mohsinharoon77/create-an-ai-chatbot-for-your-business-using-openai-dialogflow-and-chatgpt"><img class="adapt-img p_image" src="https://imgtr.ee/images/2023/12/16/c17ecf20720b43afcab9e66cc4962284.png" alt style="display: block;" width="300"></a></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td><td dir="ltr" width="20"></td><td dir="ltr" width="260" valign="top"><![endif]-->
                                                        <table cellpadding="0" cellspacing="0" class="es-left" align="left">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="260" align="left" class="esd-container-frame">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr class="es-mobile-hidden">
                                                                                    <td align="center" class="esd-block-spacer" height="130"></td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-p5b" esd-links-underline="none">
                                                                                        <h2><a target="_blank" style="text-decoration: none;" href="https://www.fiverr.com/mohsinharoon77/create-an-ai-chatbot-for-your-business-using-openai-dialogflow-and-chatgpt">Order Our AI & Chatbot Services→</a></h2>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-spacer es-p20b es-p20r es-p20l" style="font-size:0">
                                                                                        <table border="0" width="70%" height="100%" cellpadding="0" cellspacing="0" style="display: inline-table; width: 70% !important;">
                                                                                            <tbody>
                                                                                                <tr>
                                                                                                    <td style="border-bottom: 3px solid #54bab9; background: unset; height: 1px; width: 100%; margin: 0px;"></td>
                                                                                                </tr>
                                                                                            </tbody>
                                                                                        </table>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td></tr></table></td></tr></table><![endif]-->
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="esd-structure es-p40r es-m-p40l" align="left" esd-custom-block-id="819363" esdev-config="h7">
                                                        <!--[if mso]><table width="560" cellpadding="0" cellspacing="0"><tr><td width="300" valign="top"><![endif]-->
                                                        <table cellpadding="0" cellspacing="0" class="es-left" align="left">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="300" class="es-m-p20b esd-container-frame" align="left">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-image" style="font-size: 0px;"><a target="_blank" href="https://viewstripo.email"><img class="adapt-img p_image" src="https://tlr.stripocdn.email/content/guids/CABINET_829fb87b0e9e371435463b4724e5762a2905c2f1ea278b2b1beb8a6a72361d58/images/pexelsartempodrez5439898.jpeg" alt style="display: block;" width="300"></a></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td><td width="20"></td><td width="240" valign="top"><![endif]-->
                                                        <table cellpadding="0" cellspacing="0" class="es-right" align="right">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="240" align="left" class="esd-container-frame">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr class="es-mobile-hidden">
                                                                                    <td align="center" class="esd-block-spacer" height="130"></td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-p5b" esd-links-underline="none">
                                                                                        <h2><a target="_blank" style="text-decoration: none;" href="https://viewstripo.email">Shop best seller&nbsp;→</a></h2>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-spacer es-p20b es-p20r es-p20l" style="font-size:0">
                                                                                        <table border="0" width="100%" height="100%" cellpadding="0" cellspacing="0" style="width: 100% !important; display: inline-table;">
                                                                                            <tbody>
                                                                                                <tr>
                                                                                                    <td style="border-bottom: 3px solid #54bab9; background: unset; height: 1px; width: 100%; margin: 0px;"></td>
                                                                                                </tr>
                                                                                            </tbody>
                                                                                        </table>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                    </td>
                                                </tr>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table cellpadding="0" cellspacing="0" class="es-footer esd-footer-popover" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" align="center" esd-custom-block-id="819265">
                                        <table class="es-footer-body" align="center" cellpadding="0" cellspacing="0" width="600" bgcolor="rgba(0, 0, 0, 0)">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p30t es-p30b es-p20r es-p20l" align="left" esd-custom-block-id="819264">
                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="560" class="esd-container-frame" align="left">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-menu" esd-tmp-menu-padding="10|10" esd-tmp-menu-color="#ffffff" esd-tmp-divider="0|solid|#ffffff" esd-tmp-menu-font-size="12px" esd-tmp-menu-font-weight="normal">
                                                                                        <table cellpadding="0" cellspacing="0" width="100%" class="es-menu">
                                                                                            <tbody>
                                                                                                <tr class="links">
                                                                                                    <td align="center" valign="top" width="25%" class="es-p10t es-p10b es-p5r es-p5l" style="padding-bottom: 10px;"><a target="_blank" href="https://viewstripo.email" style="font-weight: normal;">About us</a></td>
                                                                                                    <td align="center" valign="top" width="25%" class="es-p10t es-p10b es-p5r es-p5l" style="padding-bottom: 10px;"><a target="_blank" href="https://viewstripo.email" style="font-weight: normal;">News</a></td>
                                                                                                    <td align="center" valign="top" width="25%" class="es-p10t es-p10b es-p5r es-p5l" style="padding-bottom: 10px;"><a target="_blank" href="https://viewstripo.email" style="font-weight: normal;">Career</a></td>
                                                                                                    <td align="center" valign="top" width="25%" class="es-p10t es-p10b es-p5r es-p5l" style="padding-bottom: 10px;"><a target="_blank" href="https://viewstripo.email" style="font-weight: normal;">The shops</a></td>
                                                                                                </tr>
                                                                                            </tbody>
                                                                                        </table>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-social es-p10t es-p10b" style="font-size:0">
                                                                                        <table cellpadding="0" cellspacing="0" class="es-table-not-adapt es-social">
                                                                                            <tbody>
                                                                                                <tr>
                                                                                                    <td align="center" valign="top" class="es-p20r" esd-tmp-icon-type="facebook"><a target="_blank" href="https://viewstripo.email"><img title="Facebook" src="https://tlr.stripocdn.email/content/assets/img/social-icons/circle-black-bordered/facebook-circle-black-bordered.png" alt="Fb" width="24" height="24"></a></td>
                                                                                                    <td align="center" valign="top" class="es-p20r" esd-tmp-icon-type="twitter"><a target="_blank" href="https://viewstripo.email"><img title="Twitter" src="https://tlr.stripocdn.email/content/assets/img/social-icons/circle-black-bordered/twitter-circle-black-bordered.png" alt="Tw" width="24" height="24"></a></td>
                                                                                                    <td align="center" valign="top" class="es-p20r" esd-tmp-icon-type="instagram"><a target="_blank" href="https://viewstripo.email"><img title="Instagram" src="https://tlr.stripocdn.email/content/assets/img/social-icons/circle-black-bordered/instagram-circle-black-bordered.png" alt="Inst" width="24" height="24"></a></td>
                                                                                                    <td align="center" valign="top" esd-tmp-icon-type="youtube"><a target="_blank" href="https://viewstripo.email"><img title="Youtube" src="https://tlr.stripocdn.email/content/assets/img/social-icons/circle-black-bordered/youtube-circle-black-bordered.png" alt="Yt" width="24" height="24"></a></td>
                                                                                                </tr>
                                                                                            </tbody>
                                                                                        </table>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-p10t es-p10b" esd-links-color="#ffffff" esd-links-underline="none">
                                                                                        <p>You are receiving this email because you have visited our site or asked us about the regular newsletter. Make sure our messages get to your Inbox (and not your bulk or junk folders).<br><a target="_blank" href="https://viewstripo.email">Privacy police</a> | <a target="_blank">Unsubscribe</a></p>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</body>

</html>
"""

html_part = MIMEText(html_content, "html")
message.attach(html_part)

try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, rec_email, message.as_string())
    print('Email sent successfully to ', "!")
except Exception as e:
    print(f'An error occurred: {e}')
