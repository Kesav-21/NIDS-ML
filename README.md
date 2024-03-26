# Network Intrustion Detection System Using Learning Based Approaches

## Abstract

Network Intrusion Detection Systems (NIDS) play a critical role in protecting computer networks from various security threats and attacks. As the complexity and frequency of network attacks continue to evolve, there is a growing need for advanced analytics techniques to enhance the detection and response capabilities of NIDS. This research focuses on the development and utilization of analytics methods for network intrusion detection systems. The goal is to leverage these techniques to improve the accuracy, efficiency, and effectiveness of NIDS in identifying and mitigating security breaches. The research begins by exploring the fundamental concepts of network intrusion detection, including the different types of attacks and the challenges associated with their detection. Various types of NIDS, including signature-based and anomaly-based systems, are discussed, highlighting their strengths and limitations. Overall, this research aims to advance the field of network intrusion detection by leveraging analytics techniques to enhance the capabilities of NIDS. The proposed methods offer the potential to improve the accuracy of attack detection, reduce false positives, enable efficient processing of big data, and facilitate automated incident response. The findings of this research will contribute to the development of more robust and effective network security systems in the face of ever-evolving cyber threats.

## Installation

Install The required Library for the Project

`pip install -r /path/to/requirements.txt `

Run The Project By following the Steps

1. Open the terminal and change the path to the project deploy folder
2. Type in the following command 
`py manage.py runserver`
3. Visit the [127.0.0.1:8000](http://127.0.0.1:8000)

## Description of Dataset

1. duration: The length of time (in seconds) for which the connection lasted.

2. protocol_type: The protocol type of the connection (e.g., TCP, UDP, ICMP).

3. service: The network service or application being accessed or used in the connection (e.g., HTTP, FTP, SSH).

4. flag: Different flags or status indicators associated with the connection (e.g., FIN, SYN, RST).

5. src_bytes: The number of bytes sent from the source to the destination in the connection.

6. dst_bytes: The number of bytes sent from the destination to the source in the connection.

7. land: Indicates whether the connection is from/to the same host/port (1 if connection is from/to the same host/port; otherwise, 0).

8. wrong_fragment: The number of "wrong" fragments in the connection.

9. urgent: Indicates the presence of urgent data in the connection.

10. hot: The number of "hot" indicators in the connection.

11. num_failed_logins: The number of failed login attempts.

12. logged_in: Indicates whether the user was logged in (1 if logged in; otherwise, 0).

13. num_compromised: The number of compromised conditions.

14. root_shell: Indicates whether root shell access was obtained (1 if yes; otherwise, 0).

15. su_attempted: Indicates whether "su" command was attempted (1 if attempted; otherwise, 0).

16. num_root: The number of root accesses.

17. num_file_creations: The number of file creations.

18. num_shells: The number of shell prompts.

19. num_access_files: The number of access control files.

20. num_outbound_cmds: The number of outbound commands.

21. is_host_login: Indicates whether the login belongs to the "host" category (1 if yes; otherwise, 0).

22. is_guest_login: Indicates whether the login belongs to the "guest" category (1 if yes; otherwise, 0).

23. count: The number of connections to the same host as the current connection.

24. srv_count: The number of connections to the same service as the current connection.

25. serror_rate: The percentage of connections that have "SYN" errors.

26. srv_serror_rate: The percentage of connections to the same service that have "SYN" errors.

27. rerror_rate: The percentage of connections that have "REJ" errors.

28. srv_rerror_rate: The percentage of connections to the same service that have "REJ" errors.

29. same_srv_rate: The percentage of connections to the same service.

30. diff_srv_rate: The percentage of connections to different services.

31. srv_diff_host_rate: The percentage of connections to different hosts for the same service.

32. dst_host_count: The number of connections to the same destination host.

33. dst_host_srv_count: The number of connections to the same destination host's service.

34. dst_host_same_srv_rate: The percentage of connections to the same service on the same destination host.

35. dst_host_diff_srv_rate: The percentage of connections to different services on the same destination host.

36. dst_host_same_src_port_rate: The percentage of connections from the same source port to the same destination host.

37. dst_host_srv_diff_host_rate: The percentage of connections to the same service but to different hosts on the same destination host.

38. dst_host_serror_rate: The percentage of connections that have "SYN" errors on the destination host.

39. dst_host_srv_serror_rate: The percentage of connections to the same service that have "SYN" errors on the destination host.

40. dst_host_rerror_rate: The percentage of connections that have "REJ" errors on the destination host.

41. dst_host_srv_rerror_rate: The percentage of connections to the same service that have "REJ" errors on the destination host.

42. xAttack: The target variable indicating whether an intrusion attack has occurred or not. This column typically contains labels such as "normal" or the type of intrusion attack if one is detected.

