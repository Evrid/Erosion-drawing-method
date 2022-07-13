
clear; close all; clc; rng('default');   %clear previous stuff

SumMatrix=dlmread('test.txt');

%disp(size(SumMatrix,1));


for xx=1:size(SumMatrix,1)-1
 if SumMatrix(xx,3)~=0  %is Z is not on paper then we draw null
 SumMatrix(xx,1)=NaN;
 SumMatrix(xx,2)=NaN;
 end
%plot([SumMatrix(xx,1),SumMatrix(xx+1,1)], [SumMatrix(xx,2),SumMatrix(xx+1,2)],'color',[0.5,0.5,0.5],'LineWidth',3 );  %display dynamic plotting  
 
 %drawnow;
% hold on;

end

plot(SumMatrix(:,1),SumMatrix(:,2),'color',[0.5,0.5,0.5],'LineWidth',4); 
hold on;

ax = gca;
exportgraphics(ax,'TestGraph.png','Resolution',300);

writematrix(SumMatrix,'test2.txt');  

