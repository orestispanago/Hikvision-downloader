#include "public.h"
#include "CapPicture.h"
#include <stdio.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <strstream>
#include <unistd.h>

#define BUF_LEN 3 * 1024 * 1024 // SHOULD BE READ FROM DEVICE CONFIG
const int devChnl = 2;

int Demo_Capture()
{
    NET_DVR_Init();
    long lUserID;
    //login
    NET_DVR_USER_LOGIN_INFO struLoginInfo = {0};
    NET_DVR_DEVICEINFO_V40 struDeviceInfoV40 = {0};
    struLoginInfo.bUseAsynLogin = false;

    struLoginInfo.wPort = 8000;
    memcpy(struLoginInfo.sDeviceAddress, "150.140.194.27", NET_DVR_DEV_ADDRESS_MAX_LEN);
    memcpy(struLoginInfo.sUserName, "admin", NAME_LEN);
    memcpy(struLoginInfo.sPassword, "Yourpassword", NAME_LEN);

    lUserID = NET_DVR_Login_V40(&struLoginInfo, &struDeviceInfoV40);

    if (lUserID < 0)
    {
        printf("pyd1---Login error, %d\n", NET_DVR_GetLastError());
        return HPR_ERROR;
    }


    NET_DVR_JPEGPICTURE_WITH_APPENDDATA data = {0};
    data.pJpegPicBuff = new char[BUF_LEN];
    memset(data.pJpegPicBuff, 0, BUF_LEN);
    data.pP2PDataBuff = new char[BUF_LEN];
    memset(data.pP2PDataBuff, 0, BUF_LEN);
    data.pVisiblePicBuff = new char[BUF_LEN];
    memset(data.pVisiblePicBuff, 0, BUF_LEN);

    int iRet;
    iRet = NET_DVR_CaptureJPEGPicture_WithAppendData(lUserID, devChnl, &data);
    if (!iRet)
    {
        printf("pyd1---NET_DVR_CaptureJPEGPicture error, %d\n", NET_DVR_GetLastError());
        return HPR_ERROR;
    }

    // printf("pyd---Channel %d dwP2PDataLen is %u.\n", devChnl, data.dwP2PDataLen);
    // printf("pyd---Channel %d dwJpegPicWidth is %u.\n", devChnl, data.dwJpegPicWidth);
    // printf("pyd---Channel %d dwJpegPicHeight is %u.\n", devChnl, data.dwJpegPicHeight);

    char fname[1024];
    struct tm *timenow;
    time_t now = time(NULL);
    timenow = gmtime(&now);
    strftime(fname, sizeof(fname), "%Y%m%d_%H%M%S", timenow);

    auto dump2file = [](std::string fname, char *d, int dsize)
    {
        std::ofstream f(fname, std::ios::out | std::ios::binary);
        f.write((char *)d, dsize);
        f.close();
    };
    std::string s;
    s+=fname;

    dump2file(s+".dat", data.pP2PDataBuff, data.dwP2PDataLen);
    dump2file(s+"_t.jpeg", data.pJpegPicBuff, data.dwJpegPicLen);
    dump2file(s+"_v.jpeg", data.pVisiblePicBuff, data.dwVisiblePicLen);

    // logout
    NET_DVR_Logout_V30(lUserID);
    NET_DVR_Cleanup();

    return HPR_OK;
}
