���ڻ������ã�

��Ҫ pip install azure 
azure �汾�����1.0�� ����汾����1.0��������ж���ٰ�װ��
�鿴azure �汾 pip freeze
�����뿴��https://github.com/Azure/azure-storage-python


�����ļ���
AzureTableHelper.py�� Ϊ��ѯ���ļ�����װ�˵�¼�������Լ�table�Ĳ�ѯ�롣
mathtool.py�� ��װ��һЩ���㷽����AzureTableHelper.py ����ø�ģ���м���ʱ��ķ�������ģ�����ݲ��ö���
taskscript_config.py�� ��װ��¼��Ϣ�����ݲ��ö���AzureTableHelper.py ����á�
deviceMode.csv: �豸�ͺű�
deviceType.csv���豸���ͱ�
station.csv�������վ��
taskfiles:ΪһЩ�豸�ļ�



����AzureTableHelper.py��

ReadAzureTable ���еķ��� readData��Ϊ��ѯtable���ݵķ�����
��������Ϊ���豸��ţ��豸���ͱ�ţ���ʼʱ�䣬����ʱ�䡣�Ѿ�����ģ�塣
��ѯֻ���ѯĳһ���豸�����ݣ���Ҫ��ѯһ���豸�����������豸�����ݣ���Ҫдһ��ѭ�������в�ѯ��
ÿһ���豸�������ж��ٸ��豸�������豸����Ƕ��٣����Բο���http://p.cnecloud.cn/  �˺ţ�raoyb, ���룺rao@2017
��ڣ������� -- �豸��Ϣ -- ɸѡ��վ���ƣ��豸���ƣ��豸�ͺţ� �ɲ鿴���豸�ͺ��µ��豸��š�


����table ��ѯ�﷨��

��readData �����У�filter_string Ϊ��ѯ�﷨��û�йؼ��֣�ֻ������ɸѡ���ɣ�����--eq ����--gt С�� --lt ���ڵ���--ge С�ڵ���--le
Ŀǰ���нṹΪһ��partitionKey Ϊһ���豸�� ���� partitionKey eq 2����ʾ����Ҫ�����豸�����2�����ݡ�


����table�У���������˼��

partitionKey : һ��Ϊһ���豸һ��key������ƽԭ��վ�Ļ�����10��partitionKey Ϊ10
RowKey: Ϊʱ�䣬��mathtool.py�ļ��У��Ѿ�����������
c: �豸��ţ�һ����partitionKey ��ֵ��ͬ
m: �豸�ͺű��룬������ʽΪ ��վ���� + M + �豸���� + M + �ͺű��룬 ��������csv�ļ��в鵽��
������������ο���http://p.cnecloud.cn/ �˺ţ�raoyb, ���룺rao@2017
��ڣ������� -- �豸�ͺŵ�� ɸѡ�����󣬿ɲ鵽��˼��


����main.py:
�����ײ�����ã��ļ���ʽΪ"�豸����_����" �����Լ�����һ�¡�
��Ҫ�Լ���ѡ��ĳһ����վ��ѡ��ĳһ����վ���޸�stationDevicedevice������
����ƽԭ��վ����д��stationDevicedevice = s350.allDevice�� �˶�Ϊ  stationDevicedevice = s340.allDevice
���Լ�����ı����У� path ·����deviceType �豸���ʹ��� int ���ͣ� ������devicetypelist ������豸���͵�һ���б�
��datelist �����һ�������б�ÿ��Ԫ��Ϊһ������Ϊ�����б�����0Ϊ��ʼʱ�䣬����1Ϊ����ʱ�䣬�Ӷ�����ѭ��һֱ�������ݡ�
ѭ�������Ѿ�����������ע���ˡ�

�����κ����⾴����ϵ������� raoyb@cnegroup.com