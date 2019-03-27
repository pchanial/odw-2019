# odw-challenge

Challenge activity for Open Data Workshop 2019: https://indico.in2p3.fr/event/18313/

Data files are available at https://dcc.ligo.org/LIGO-T1900135/public

## Excercise 1

Identify a loud binary black hole signal in white, Gaussian noise.

* Use the data file "challenge1.gwf".  The channel name is "H1:CHALLENGE1".
* The data are  white, Gaussian noise containing a simulated BBH signal.

1. Load the data into memory.  What are the sampling rate and duration of the data?

2. Plot the data as a time-domain signal. 

3. Plot a spectrogram (or q-transform) of the data, and try to identify the signal.

4. What is the time of the signal?


## Excercise 2

Signal in colored, Gaussian noise.

* Use the data file "challenge2.gwf", with channel name "H1:CHALLENGE2"
* The data contain a BBH signal with m1=m2=30 solar masses, spin = 0.


1. What is the time of the merger? (Hint: a plot of the q-transform could help)

2. Generate and a time-domain template waveform using approximate "SEOBNRv4_opt".  Plot this
waveform.

3. Calculate a PSD of the data, and plot this on a log-log scale.
Use axes ranging from 20 Hz up to the Nyquist frequency.

4. Use the template waveform and PSD to calculate the SNR time series.  Plot the SNR time-series.

5. What is the matched filter SNR of the signal?


### Excercise 3

* Use the data file ./challenge3.gwf" with channel "H1:CHALLENGE3"
* These are real LIGO data from O2, though we've adjusted the time labels and 
  added some simulated signals.
* The data contain a loud simulated singal with m1 = m2 = 10 solar masses.

1. What is the merger time of this 10/10 signal?

2. What is the matched-filter SNR of this 10/10  signal?


### Excercise 4

* Use the data file ./challenge3.gwf" with channels "H1:CHALLENGE3" and "L1:CHALLENGE3".
* These are real LIGO data from O2, though we've adjusted the time labels and 
  added some simulated signals.
* Any simulated signals have been added to both the H1 and L1 data
* All simulated signals have 0 spin and m1=m2, with m1 somewhere in the range 10-50 solar masses

1. Identify as many signals as you can.  Watch out!  These are real data, and so glitches may be
present.  Any false alarms will count against your score.  For each signal you find, list:

 * The merger time
 * The SNR
 * Your estimate of the component masses

2. Identify as many glitches as you can.  Make a spectrogram of each one.

3. For each simulated BBH you found, use Bilby to compute a
posterior distribution for the mass.  You can fix the spin and sky
location parameters to make this run faster.
