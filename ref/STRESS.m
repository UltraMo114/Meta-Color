function STRESS=STRESS(dEi,dVi)
%calculate STRESS performance metric
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  F1=sum(dEi.^2)./sum(dEi.*dVi);
% STRESS1=sqrt(sum((dEi-F1.*dVi).^2)./sum((dEi).^2));
STRESS= 100 * sqrt(1-((sum(dEi.*dVi)).^2)/(sum(dEi.^2).*sum(dVi.^2)));
% STRESS = [STRESS1,STRESS_];
end